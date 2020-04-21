from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from acserver.models import Server, Car, Track
from .forms import UploadFileForm, UpdateCarForm, UpdateTrackForm
from .utils import unzip_pack, read_server_cfg, write_server_cfg, exec_command, upgrade_pack


@login_required
def manager(request):
    request.session.set_expiry(0)
    context = {
        "servers": Server.objects.all(),
        "cars": Car.objects.all(),
        "tracks": Track.objects.all()
    }
    return render(request, 'manageserver/task.html', context)

@login_required
def upload(request):
    request.session.set_expiry(0)
    context = {}
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            server = Server.objects.get(pk=int(form.cleaned_data['all_servers']))
            file = request.FILES['file']
            if unzip_pack(file, server):
                return redirect(reverse('manageserver:upload'))

        else:
            context['errors'] = form.errors.items()

    else:
        form = UploadFileForm()
        form_car = UpdateCarForm()
        form_track = UpdateTrackForm()
        context['form'] = form
        context['form_car'] = form_car
        context['form_track'] = form_track

    return render(request, 'manageserver/addcontent.html', context)

@login_required
def update_database(request):
    if request.method == "POST":
        if request.POST['form_identifiant'] == 'car':
            car = Car()
            form = UpdateCarForm(request.POST)
            if form.is_valid():
                car_name = form.cleaned_data['name_car']
                car_folder = form.cleaned_data['name_folder']
                if 'is_car_addon' in request.POST.keys():
                    addon = True
                else:
                    addon = False
                car.name = car_name
                car.folder_name = car_folder
                car.addon = addon
                car.save()

        elif request.POST['form_identifiant'] == 'track':
            track = Track()
            form = UpdateTrackForm(request.POST)
            if form.is_valid():
                track_name = form.cleaned_data['name_track']
                track_folder = form.cleaned_data['name_folder']
                if 'is_track_addon' in request.POST.keys():
                    addon = True
                else:
                    addon = False
                track.name = track_name
                track.folder_name = track_folder
                track.addon = addon
                track.save()

        return redirect(reverse('manageserver:upload'))

@login_required
def edit_cfg(request, id_server):
    request.session.set_expiry(0)
    server = Server.objects.get(pk=id_server)

    if request.method == 'POST':
        new_config = request.POST['new_config']

        if write_server_cfg(server.file_cfg, new_config):
            return JsonResponse({'status': 'updated'})
        else:
            return JsonResponse({'status': 'not-updated'})        

    else:
        context = {}
        
        context['file_cfg'] = read_server_cfg(server.file_cfg)
        context['server_name'] = server.name
        return render(request, 'manageserver/editcfg.html', context)

@login_required
def edit_car_list(request, id_server):
    request.session.set_expiry(0)
    server = Server.objects.get(pk=id_server)

    if request.method == 'POST':
        new_config = request.POST['new_config']

        if write_server_cfg(server.file_entry_list, new_config):
            return JsonResponse({'status': 'updated'})
        else:
            return JsonResponse({'status': 'not-updated'})

    else:
        context = {}
        context['file_car_list'] = read_server_cfg(server.file_entry_list)
        context['server_name'] = server.name
        return render(request, 'manageserver/editcarlist.html', context)

@login_required
def run_reboot_stop_server(request, id_server, cmd):
    server = Server.objects.get(pk=id_server)

    result = exec_command(server, cmd)

    if result['check']:
        return JsonResponse({"error": False, "status_cmd": result['res']})
    else:
        return JsonResponse({"error": True})

@login_required
def update_pack(request):
    if request.method == 'POST':
        server = Server.objects.get(pk=request.POST['server'])
        server.cars.clear()

        cars = request.POST['cars'].split(',')
        cars_objects = []
        for i in cars:
            car = Car.objects.get(pk=int(i))
            server.cars.add(car)
            cars_objects.append(car)
        
        track = Track.objects.get(pk=int(request.POST['track']))
        server.track = track
        server.save()

        upgrade_pack(server, cars_objects, track)

        return JsonResponse({'updated': True})
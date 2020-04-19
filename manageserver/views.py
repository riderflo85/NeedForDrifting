from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from acserver.models import Server
from .forms import UploadFileForm
from .utils import unzip_pack, read_server_cfg, write_server_cfg, exec_command


@login_required
def manager(request):
    request.session.set_expiry(0)
    context = {"servers": Server.objects.all()}
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
        form_car = UploadFileForm()
        form_track = UploadFileForm()
        context['form_car'] = form_car
        # context['form_track'] = form_track

    return render(request, 'manageserver/addcontent.html', context)

@login_required
def edit_cfg(request, id_server):
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
    print(server.name_cmd+' '+cmd+' res cmd '+str(result))
    if result['check']:
        return JsonResponse({"error": False, "status_cmd": result['res']})
    else:
        return JsonResponse({"error": True})

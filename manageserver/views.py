from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from acserver.models import Server
from .forms import UploadFileForm
from .utils import unzip_pack


@login_required
def manager(request):
    return render(request, 'manageserver/task.html')

@login_required
def upload(request):
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
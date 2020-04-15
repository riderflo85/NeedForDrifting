import os
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, FileResponse
from .models import Server


def index(request):
    context = {}
    context['servers'] = Server.objects.all()
    return render(request, 'acserver/index.html', context)

def download(request, id_server):
    server = get_object_or_404(Server, id=id_server)
    zip_name = f"{server.name.replace(' ', '_')}.zip"
    os.system(f"cd {server.path_upload} && zip -r {zip_name} cars tracks")
    file_path = server.path_upload + zip_name
    zip_file = open(file_path, 'rb')
    res = FileResponse(zip_file, as_attachment=True, content_type="application/zip")
    return res
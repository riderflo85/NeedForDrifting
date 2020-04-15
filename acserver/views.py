from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Server


def index(request):
    context = {}
    context['servers'] = Server.objects.all()
    return render(request, 'acserver/index.html', context)

def download(request):
    if request.method == "POST":
        id_server = request.POST['id_server']
        server = get_object_or_404(Server, id=id_server)
        # envoi les fichiers au client
        return JsonResponse({'success': True})


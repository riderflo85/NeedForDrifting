from django.shortcuts import render
from .models import Server


def index(request):
    context = {}
    context['servers'] = Server.objects.all()
    return render(request, 'acserver/index.html', context)
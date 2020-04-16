from django.shortcuts import render


def manager(request):
    return render(request, 'manageserver/task.html')
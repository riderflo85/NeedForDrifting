from django.shortcuts import render


def manager(request):
    return render(request, 'manageserver/task.html')

def upload(request):
    return render(request, 'manageserver/addcontent.html')
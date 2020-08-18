from django.shortcuts import render
from django.http import JsonResponse
from .models import UserAC
from .decorator import check_token

# rendre unique le token dans la BDD
@check_token
def check_login_user(request):
    response = {'error': False}
    if request.method == 'GET': # changer la méthode GET en POST
        username = request.GET['username']
        password = request.GET['pwd']
        user = UserAC.objects.get(username=username)
        
        if user.check_password(password):
            response['user_authenticated'] = True
            return JsonResponse(response)

        else:
            response['error'] = True
            return JsonResponse(response)
    else:
        response['error'] = True
        return JsonResponse(response)

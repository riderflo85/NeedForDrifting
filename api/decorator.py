from django.http import JsonResponse, HttpResponseNotFound
from .models import UserAC


def check_token(function):

    def if_user_token(request, *args, **kwargs):
        api_key = request.GET['api']
        username = request.GET['username']
        user = UserAC.objects.filter(username=username).filter(token=api_key)

        if len(user) == 1:
            return function(request, *args, **kwargs)
        else:
            return JsonResponse({'error': True})

    return if_user_token
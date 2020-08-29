from django.http import JsonResponse
from acserver.models import Server, Track
from manageserver.utils import exec_command
from .models import UserAC
from .decorator import check_token
from .utils import servers_to_json, update_track


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


@check_token
def get_all_servers(request):
    response = {'error': False}
    if request.method == 'GET':
        servers = Server.objects.all()
        dict_servers = servers_to_json(servers)
        response['servers'] = dict_servers
        return JsonResponse(response)

    else:
        response['error'] = True
        return JsonResponse(response)


@check_token
def run_cmd(request):
    response = {'error': False}
    if request.method == 'GET':
        id_server = request.GET['server_id']
        command = request.GET['server_cmd']
        server = Server.objects.get(pk=int(id_server))
        res = exec_command(server, command)
        response['state'] = res

        return JsonResponse(response)

    else:
        response['error'] = True
        return JsonResponse(response)


@check_token
def change_track(request):
    response = {'error': False}
    if request.method == 'GET':
        id_server = request.GET['server_id']
        id_track = request.GET['track_id']
        config_track = request.GET['config_track']
        max_clients = request.GET['max_clients']

        server = Server.objects.get(pk=int(id_server))
        track = Track.objects.get(pk=int(id_track))

        done = update_track(server, track, config_track, max_clients)
        response['state'] = done

        return JsonResponse(response)

    else:
        response['error'] = True
        return JsonResponse(response)

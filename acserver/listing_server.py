import subprocess
from .models import Server


def list_all_servers():
    servers = []

    for serv in Server.objects.all():
        servers.append((serv.pk, serv.name))

    return servers

def list_all_cars():
    cars = []

    for serv in Server.objects.all():
        cmd = serv.path_download + "content/cars/"
        res = subprocess.check_output(['ls', cmd]).decode('utf-8')
        res = res.split('\n')
        res.pop(-1)
        for car in res:
            if (car, car) not in cars:
                cars.append((car, car))

    return cars

def list_all_tracks():
    tracks = []

    for serv in Server.objects.all():
        cmd = serv.path_download + "content/tracks/"
        res = subprocess.check_output(['ls', cmd]).decode('utf-8')
        res = res.split('\n')
        res.pop(-1)
        for track in res:
            if (track, track) not in tracks:
                tracks.append((track, track))

    return tracks
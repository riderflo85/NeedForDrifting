from .models import Server


def list_all_servers():
    servers = []

    for serv in Server.objects.all():
        servers.append((serv.pk, serv.name))

    return servers
def servers_to_json(servers):
    """
    Convert the QuerySet object to the JSON object for sending to the mobile app.
    """

    dict_servers = []

    count = 1
    for server in servers:
        dict_servers.append({
            'id': str(server.id),
            'name': server.name,
            'status': server.status,
            'track': server.track.name
        })
        count = count + 1

    return dict_servers
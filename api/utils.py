def servers_to_json(servers):
    """
    Convert the QuerySet object to the JSON object for sending to the mobile app.
    """

    list_servers = []

    for server in servers:
        list_servers.append({
            'id': str(server.id),
            'name': server.name,
            'status': server.status,
            'track': server.track.name
        })

    return list_servers


def tracks_to_json(tracks):
    """
    Convert the QuerySet object to the JSON object for sending to the mobile app.
    """

    list_tracks = []

    for track in tracks:
        list_tracks.append({
            'id': str(track.id),
            'name': track.name,
            'folder_name': track.folder_name
        })

    return list_tracks


def update_track(server, new_track, new_config_track, max_clients):
    """
    Update the config file for change the track in this server.
    """

    new_data = []

    try:
        with open(server.file_cfg, 'r') as file:
            data = file.readlines()

            for line in data:
                new_line = line.replace('\n', '')

                if new_line.startswith('TRACK='):
                    track = new_line
                    index_equal = track.find('=')
                    track = track[:index_equal+1] + new_track.folder_name + '\n'
                    new_data.append(track)

                elif new_line.startswith('CONFIG_TRACK='):
                    config_track = new_line
                    index_equal = config_track.find('=')
                    config_track = config_track[:index_equal+1]
                    config_track = config_track + new_config_track + '\n'
                    new_data.append(config_track)
                
                elif new_line.startswith('MAX_CLIENTS='):
                    client = new_line
                    index_equal = client.find('=')
                    client = client[:index_equal+1] + max_clients + '\n'
                    new_data.append(client)
                
                else:
                    new_data.append(line)

        with open(server.file_cfg, 'w') as file:
            file.writelines(new_data)

        server.track = new_track
        server.save()

        return True

    except:
        return False

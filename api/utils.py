def servers_to_json(servers):
    """
    Convert the QuerySet object to the JSON object for sending to the mobile app.
    """

    dict_servers = []

    for server in servers:
        dict_servers.append({
            'id': str(server.id),
            'name': server.name,
            'status': server.status,
            'track': server.track.name
        })

    return dict_servers


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
                    track = track[:index_equal+1] + new_track + '\n'
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

        return True

    except:
        return False

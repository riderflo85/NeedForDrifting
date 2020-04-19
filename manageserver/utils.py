import os
from acserver.models import Server


def unzip_pack(file, server):
    """ Unzip the files pack in the folder on the server """

    if file.name == "cars.zip":
        path = server.path_download
        path = path + "content/cars/"
    elif file.name == "track.zip":
        path = server.path_download
        path = path + "content/tracks/"

    file_path = path + file.name
    with open(file_path, 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)
    
    if file.name in os.listdir(path):
        os.system(f"cd {path} && unzip {file.name} && rm {file.name}")

        return True

    else:
        return False

def read_server_cfg(path_file):
    """ Read the server settings """

    content_file = ""
    with open(path_file, 'r') as file:
        content_file = file.read()

    return content_file

def write_server_cfg(path_file, content):
    """ Write the new settings in the files server """

    try:
        with open(path_file, 'w') as file:
            file.write(content)

        return True

    except:
        return False
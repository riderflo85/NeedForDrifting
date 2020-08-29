import os
import subprocess


def unzip_pack(file, server):
    """ Unzip the files pack in the folder on the server """

    path = ''

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

def exec_command(server, cmd):
    try:
        res = subprocess.check_output(["./acManager.sh",server.name_cmd,cmd])
        res = res.decode('utf-8').replace('\n', '')

        if res == "run":
            server.status = "running"
        elif res == "kill":
            server.status = "stoping"
        else:
            server.status = res
        
        server.save()

        return {"check": True, "res": res}
    except:
        return {"check": False}

def upgrade_pack(server, list_cars, track):
    car_dir = server.path_download + "content/cars/"
    track_dir = server.path_download + "content/tracks/"
    zip_name = f"{server.name.replace(' ', '_')}.zip"
    file_path = server.path_upload + zip_name

    try:
        os.system(f"rm {file_path}")
        os.system(f'rm -r {server.path_upload}cars/*')
        os.system(f'rm -r {server.path_upload}tracks/*')
    except:
        pass    

    for car in list_cars:
        if car.addon:
            os.system(f"cp -r '{car_dir}{car.folder_name}' {server.path_upload}cars/")

    if track.addon:
        os.system(f"cp -r '{track_dir}{track.folder_name}' {server.path_upload}tracks/")

import json
import os
import subprocess
import threading
import minecraft_launcher_lib as mll

user_windows = os.environ["USERNAME"]
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"
ruta_json = f"{minecraft_directory}//configuration.json"
ruta_java = f"{minecraft_directory}//runtime//jre-legacy//windows-x64//jre-legacy//bin//java.exe"

def latest_versions():
    versiones = []
    version = mll.utils.get_installed_versions(minecraft_directory)
    for ver in version:
        if ver["type"] == "release":
            versiones.append(ver["id"])
    return versiones

def list_versions():
    versioneslis = []
    versionlis = mll.utils.get_version_list()
    for ver in versionlis:
        if ver["type"] == "release" or ver["type"] == "snapshot":
            versioneslis.append(ver["id"])
    return versioneslis


def save_config(mine_user=None, uuid=None, version=None, ram=None, java=None):
    # Verificar si el archivo existe
    if not os.path.exists(ruta_json):
        # Si no existe, crear el diccionario con los valores proporcionados
        data = {
            "username": mine_user if mine_user is not None else "",
            "uuid": uuid if uuid is not None else "",
            "token": "",
            "ram": ram if ram is not None else "",
            "version": version if version is not None else "",
            "java": java if java is not None else "",
        }
    else:
        # Si el archivo existe, cargar los datos existentes
        with open(ruta_json, "r") as f:
            data = json.load(f)

    # Actualizar los valores solo si se pasan en la función
    if mine_user is not None:
        data["username"] = mine_user
    if uuid is not None:
        data["uuid"] = uuid
    if version is not None:
        data["version"] = version
    if ram is not None:
        data["ram"] = ram
    if java is not None:
        data["java"] = java

    # Guardar los datos actualizados en el archivo
    with open(ruta_json, "w") as f:
        json.dump(data, f, indent=4)

# def launch_minecraft(e):
#     # Crear y comenzar un hilo separado para ejecutar play_mine
#     threading.Thread(target=play_mine).start()


async def play_mine(e):
    global options
    if os.path.exists(ruta_json):
        with open(ruta_json, "r") as file:
            data = json.load(file)

        if "username" in data and "ram" in data:
            mine_user = data["username"]
            version = data["version"]
            ram = data["ram"]
            java= data["java"]
            
            # uuid = data["uuid"]
        # if uuid == "" or uuid == None:
        #     info = mll.utils.generate_test_options()
        #     save_config(uuid=info["uuid"])

        
        options = {
            "username": mine_user,
            "uuid": '',
            "token": "",
            "executablePath": java, 
            "defaultExecutablePath": ruta_java,
            "jvmArguments": [
                f"-Xmx{ram}G",
                f"-Xms{ram}G",
            ],  # The jvmArguments
            "launcherVersion": "1.0.0",
        }

        # Ejecutar Minecraft
        minecraft_command = mll.command.get_minecraft_command(
            version, minecraft_directory, options
        )
        subprocess.run(minecraft_command, 
                       creationflags=subprocess.CREATE_NO_WINDOW

                    )
    else:
        print('error')
        pass

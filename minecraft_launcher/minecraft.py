import json
import os
import subprocess

import minecraft_launcher_lib

user_windows = os.environ["USERNAME"]
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"
ruta_json = f"{minecraft_directory}//configuracion.json"


async def prueba(e):
    print(e)
    await play_mine()


async def play_mine():
    global options
    with open(ruta_json, "r") as file:
        data = json.load(file)

    if "Nombre" in data and "RAM" in data:
        mine_user = data["Nombre"]
        version = data["Version"]
        ram = data["RAM"]
        java_ruta = data.get("Java", None)

    options = {
        "username": mine_user,
        "uuid": "",
        "token": "",
        "executablePath": f"{java_ruta}",
        "jvmArguments": [
            f"-Xmx{ram}G",
            f"-Xms{ram}G",

        ],  # The jvmArguments
        "launcherVersion": "1.0.0",
    }

    # Ejecutar Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
        version, minecraft_directory, options
    )  # type: ignore
    subprocess.run(minecraft_command)

import os
import flet as ft
import minecraft_launcher_lib as mll
import json

from minecraft_launcher.minecraft import latest_versions, save_config

user_windows = os.environ["USERNAME"]
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"

# Ruta del archivo de configuración
ruta_json = f"{minecraft_directory}//configuration.json"

# Verificar si el archivo de configuración existe y cargar datos si existe
if os.path.exists(ruta_json):
    with open(ruta_json, 'r') as file:
        config_data = json.load(file)
else:
    config_data = {
        "mine_user": "",
        "ram": "",
        "version": ""
    }

# Obtiene la lista de versiones instaladas
versions = latest_versions()
opciones = [ft.dropdown.Option(version) for version in versions]

title = ft.Text('Perfil', font_family='mine_dun', size=30)

username = ft.TextField(
    hint_text="User Name",
    width=250,
    height=50,
    bgcolor='#343434',
    border=ft.InputBorder.NONE,
    border_radius=30,
    cursor_height=20,
    text_style=ft.TextStyle(
        font_family='mine',
        size=15,
    ),
    value=config_data.get("mine_user", "")
)

ram = ft.TextField(
    hint_text="RAM",
    width=250,
    height=50,
    bgcolor='#343434',
    border=ft.InputBorder.NONE,
    border_radius=30,
    cursor_height=20,
    text_style=ft.TextStyle(
        font_family='mine',
        size=15,
    ),
    value=config_data.get("ram", "")
)

version = ft.Dropdown(
    width=250,
    height=50,
    bgcolor="#343434",
    focused_bgcolor="#343434",
    border=ft.InputBorder.NONE,
    text_style=ft.TextStyle(
        font_family='mine',
        size=15,
    ),
    options=opciones,
    value=config_data.get("version", "")
)

def save_configuration(e):
    config = {
        "mine_user": username.value,
        "ram": ram.value,
        "version": version.value
    }
    with open(ruta_json, 'w') as file:
        json.dump(config, file)

guardar_btn = ft.ElevatedButton(
    "Guardar",
    style=ft.ButtonStyle(
        color="#ffffff",
        bgcolor="#68C90E",
        overlay_color="#447A12",
        shape=ft.RoundedRectangleBorder(radius=0),
        shadow_color="#178c4a",
        elevation=5,
    ),
    on_click=save_configuration,
)

user_page = ft.Stack(
    [
        ft.Container(
            content=ft.Column(
                controls=[
                    title,
                    username,
                    ram,
                    version,
                    guardar_btn,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )
    ],
    width=681,
    height=478,
)

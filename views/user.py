import os
import flet as ft
import minecraft_launcher_lib as mll

from minecraft_launcher.minecraft import latest_versions, save_config

user_windows = os.environ["USERNAME"]
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"


#Obtiene la lista de versiones instaladas
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
    text_style= ft.TextStyle(
        font_family='mine',
        size=15,
    ),
)
ram = ft.TextField(
    hint_text="RAM",
    width=250,
    height=50,
    bgcolor='#343434',
    border=ft.InputBorder.NONE,
    border_radius=30,
    cursor_height=20,
    text_style= ft.TextStyle(
        font_family='mine',
        size=15,
    ),
)
version = ft.Dropdown(
    width=250,
    height=50,
    bgcolor="#343434",
    focused_bgcolor="#343434",
    border=ft.InputBorder.NONE,
    text_style= ft.TextStyle(
        font_family='mine',
        size=15,
    ),
    options=opciones,
)
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
    on_click=lambda _: save_config(mine_user=username.value, ram=ram.value, version=version.value),
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

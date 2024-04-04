import os
import flet as ft
import minecraft_launcher_lib

user_windows = os.environ["USERNAME"]
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"

#Obtiene la lista de versiones
async def versiones(e):
    global d
    forts = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
    for fort in forts:
        d = ft.dropdown.Option(fort['id'])
        print(d)


title = ft.Text('Perfil', font_family='mine_dun', size=30)
name = ft.TextField(
    hint_text="User name",
    height=36,
    width=190,
    bgcolor='#343434',
    border=ft.InputBorder.NONE,
    border_radius=30,
    cursor_height=20,
    text_size=15
)
version = ft.Dropdown(
    width=150,
    height=40,
    bgcolor='#343434',
    focused_bgcolor='#343434',
    border=ft.InputBorder.NONE,
    on_blur=versiones,
    options=[
        ft.dropdown.Option('fabric-loader-0.15.7-1.16.5')
        
    ]
)
guardar_btn = ft.ElevatedButton("Guardar")


user_page = ft.Stack(
    [
        ft.Container(
            content=ft.Column(
                controls=[
                    title,
                    name, 
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

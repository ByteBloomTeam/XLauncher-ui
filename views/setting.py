import flet as ft
import json
import os

# Cargar configuración existente
user_windows = os.environ["USERNAME"]
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"
config_path = f"{minecraft_directory}//configuration.json"
with open(config_path, "r") as file:
    config = json.load(file)

title = ft.Text("Ajustes", font_family="mine_dun", size=30)

# Función para manejar la selección del archivo
def file_picker_result(e: ft.FilePickerResultEvent):
    if e.files:
        selected_path = e.files[0].path
        config["java"] = selected_path
        with open(config_path, "w") as file:
            json.dump(config, file, indent=4)
        java_path_text.value = selected_path
        java_path_text.update()

# Crear el FilePicker
file_picker = ft.FilePicker(on_result=file_picker_result)

# Mostrar la ruta del Java actual
java_path_text = ft.Text(config.get("java", ""), size=15, font_family='mine')

select_java_button = ft.ElevatedButton(
    text="Java",
    style=ft.ButtonStyle(
        color="#ffffff",
        bgcolor="#5B0098",
        overlay_color="#0C0C0C",
        shape=ft.RoundedRectangleBorder(radius=3),
        shadow_color="#000000",
        elevation=5,
    ),
    on_click=lambda _: file_picker.pick_files(dialog_title='Selecciona el Java', allowed_extensions=['exe'], initial_directory=minecraft_directory)
)


def create_setting_page(page):
    info_button = ft.IconButton(
        icon=ft.icons.INFO,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=lambda e: page.open(dlg)
    )

    info_text = ''' 
Launcher de Minecraft creado por Keima Senpai. El 
cual tiene el propósito de facilitar la instalación 
de Forge y Fabric. Además de tener una gran facilidad
de personalización.

'''

    dlg = ft.AlertDialog(
        title=ft.Text(
            "XLauncher v1.0.4", 
            font_family='mine',
            size=15,
            ),
        content=ft.Column(
            spacing = 5,
            controls=[
                ft.Image(src='img/logo_info.png', height=70),
                ft.Text(info_text, font_family='mine',size=12,),
                ft.Row(
                    spacing = 4,
                    controls=[
                        ft.IconButton(
                        content=ft.Image(src='img/telegram.png', height=30, width=30),
                        style=ft.ButtonStyle(
                            color="#5B0098",
                            bgcolor="#0C0C0C",
                            shape=ft.RoundedRectangleBorder(radius=5),
                        ),
                        on_click=lambda _: page.launch_url("https://t.me/+AfWKISuW0gRlMDQ5"),
                        
                    ),
                        ft.IconButton(
                        content=ft.Image(src='img/github.png', height=30, width=30),
                        style=ft.ButtonStyle(
                            color="#5B0098",
                            bgcolor="#0C0C0C",
                            shape=ft.RoundedRectangleBorder(radius=5),
                        ),
                        on_click=lambda _: page.launch_url("https://github.com/KeimaSenpai/XLauncher-ui"),
                        
                    ),
                        ft.IconButton(
                        content=ft.Image(src='img/youtube.png', height=30, width=30),
                        style=ft.ButtonStyle(
                            color="#5B0098",
                            bgcolor="#0C0C0C",
                            shape=ft.RoundedRectangleBorder(radius=5),
                        ),
                        on_click=lambda _: page.launch_url("https://www.youtube.com/@KeimaSenpaiYT"),
                        
                    ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text(
                    disabled=False,
                    spans=[
                        ft.TextSpan('Copyright © 2024.  ',
                                    ft.TextStyle(
                                        font_family='mine',
                                    )
                                ),
                        ft.TextSpan('KeimaSenpai.  ', 
                                    ft.TextStyle(
                                        font_family='mine',
                                    ),
                                    url="https://github.com/KeimaSenpai",
                                ),
                        ft.TextSpan('LICENSE', 
                                    ft.TextStyle(
                                        font_family='mine',
                                    ),
                                    url="https://github.com/KeimaSenpai/XLauncher-ui/blob/main/LICENSE",
                                ),
                    ]
                )

            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

        ),
        shape= ft.RoundedRectangleBorder(radius=5),
    )   

    setting_page = ft.Stack(
        [
            ft.Container(
                content=ft.Column(
                    controls=[
                        title,
                        java_path_text,
                        select_java_button,
                        file_picker,
                        info_button,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
            ),
        ],
        width=681,
        height=478,
    )

    return setting_page

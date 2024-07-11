# import flet as ft


# title = ft.Text('Ajustes', font_family='mine_dun', size=30)

# setting_page = ft.Stack(
#     [
#         ft.Container(
#             content=ft.Column(
#                 controls=[title],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             ),
#             alignment=ft.alignment.center,
#         ),
#     ],
#     width=681,
#     height=478,
# )


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
    text="Seleccionar ruta de Java",
    on_click=lambda _: file_picker.pick_files()
)

setting_page = ft.Stack(
    [
        ft.Container(
            content=ft.Column(
                controls=[
                    title,
                    java_path_text,
                    select_java_button,
                    file_picker
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

import flet as ft


name = ft.TextField(hint_text="User Name")
version = ft.Dropdown(
    width=100,
    options=[
        ft.dropdown.Option("Red"),
        ft.dropdown.Option("Green"),
        ft.dropdown.Option("Blue"),
    ],
)
guardar_btn = ft.ElevatedButton("Guardar")


user_page = ft.Stack(
    [
        ft.Container(
            content=ft.Column(
                controls=[name, version, guardar_btn],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        )
    ],
    width=681,
    height=478,
)

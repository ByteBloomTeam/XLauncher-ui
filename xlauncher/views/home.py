import flet as ft

from ..minecraft import prueba

minecraft_title = ft.Image(
    src="img/minecraft_title.png",
    height=170,
)

play = ft.ElevatedButton(
    "PLAY",
    style=ft.ButtonStyle(
        color="#191919",
        bgcolor="#68C90E",
        overlay_color="#447A12",
        shape=ft.RoundedRectangleBorder(radius=5),
    ),
    on_click=prueba,
)

home_page = ft.Stack(
    [
        ft.Image(
            src="img/Rectángulo.webp",
            height=478,
            width=681,
            fit=ft.ImageFit.COVER,
        ),
        ft.Container(
            content=ft.Column(
                controls=[minecraft_title, play],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        ),
    ],
    width=681,
    height=478,
)

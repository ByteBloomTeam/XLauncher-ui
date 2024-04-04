import flet as ft

from minecraft_launcher.minecraft import prueba


title = ft.Text('Instalaciones', font_family='mine_dun', size=30)

install_page = ft.Stack(
    [
        ft.Container(
            content=ft.Column(
                controls=[title],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        ),
    ],
    width=681,
    height=478,
)
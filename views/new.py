import flet as ft
import minecraft_launcher_lib as mll


title = ft.Text('Noticias', font_family='mine_dun', size=30)
# new_notice = mll.utils.get_minecraft_news
# print(new_notice)

new_page = ft.Stack(
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
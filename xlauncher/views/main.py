import flet as ft

from .home import *
from .navegacion import *


def main(page: ft.Page):
    page.title = "XLauncher"
    page.window_width = 760
    page.window_height = 478
    page.window_resizable = False
    page.padding = 0
    page.fonts = {
        "mine": "fonts/minecraft.ttf",
        "mine_dun": "fonts/minecraft-dungeons.ttf",
    }

    # Se agrupan todas las paginas
    page.add(
        ft.Row(
            spacing=0,
            controls=[nab, conte],
        )
    )


ft.app(target=main, assets_dir="assets")

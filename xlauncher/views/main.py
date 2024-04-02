import flet as ft
from .home import home_page
from .user import user_page


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

    logo = ft.Container(
        content=ft.Image(src="img/logo.webp", height=45, width=45),
        alignment=ft.alignment.center,
        height=47,
        margin=10,
    )

    a = ft.IconButton(
        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=lambda _: page.go("/"),
    )
    b = ft.IconButton(
        icon=ft.icons.ACCOUNT_CIRCLE,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
        on_click=lambda _: page.go("/user"),
    )
    c = ft.IconButton(
        icon=ft.icons.NEWSPAPER_OUTLINED,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )
    d = ft.IconButton(
        icon=ft.icons.DOWNLOAD,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )
    e = ft.IconButton(
        icon=ft.icons.SETTINGS,
        style=ft.ButtonStyle(
            color="#5B0098",
            bgcolor="#0C0C0C",
            shape=ft.RoundedRectangleBorder(radius=5),
        ),
    )
    iconos = ft.Column(controls=[a, b, c, d, e])

    # Navegacion principal de la app
    nab = ft.Container(
        content=ft.Column(
            spacing=100,
            controls=[logo, iconos],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        height=478,
        width=70,
        bgcolor="#131313",
        alignment=ft.alignment.center,
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row(
                        spacing=0,
                        controls=[
                            nab,
                            home_page,
                        ],
                    ),
                ],
                padding=0,
            )
        )
        if page.route == "/user":
            page.views.append(
                ft.View(
                    "/user",
                    [
                        ft.Row(
                            spacing=0,
                            controls=[
                                nab,
                                user_page,
                            ],
                        ),
                    ],
                    padding=0,
                )
            )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, assets_dir="assets")

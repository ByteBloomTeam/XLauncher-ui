import flet as ft

logo = ft.Container(
    content=ft.Image(src="img/logo.webp", height=45, width=45),
    alignment=ft.alignment.center,
    height=47,
    margin=10,
)

a = ft.IconButton(
    icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
    style=ft.ButtonStyle(
        color="#5B0098", bgcolor="#0C0C0C", shape=ft.RoundedRectangleBorder(radius=5)
    ),
)
b = ft.IconButton(
    icon=ft.icons.ACCOUNT_CIRCLE,
    style=ft.ButtonStyle(
        color="#5B0098", bgcolor="#0C0C0C", shape=ft.RoundedRectangleBorder(radius=5)
    ),
)
c = ft.IconButton(
    icon=ft.icons.NEWSPAPER_OUTLINED,
    style=ft.ButtonStyle(
        color="#5B0098", bgcolor="#0C0C0C", shape=ft.RoundedRectangleBorder(radius=5)
    ),
)
d = ft.IconButton(
    icon=ft.icons.DOWNLOAD,
    style=ft.ButtonStyle(
        color="#5B0098", bgcolor="#0C0C0C", shape=ft.RoundedRectangleBorder(radius=5)
    ),
)
e = ft.IconButton(
    icon=ft.icons.SETTINGS,
    style=ft.ButtonStyle(
        color="#5B0098", bgcolor="#0C0C0C", shape=ft.RoundedRectangleBorder(radius=5)
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

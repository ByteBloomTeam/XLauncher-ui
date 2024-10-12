import flet as ft

from minecraft_launcher.minecraft import play_mine



minecraft_title = ft.Image(
    src="img/minecraft_title.png",
    height=170,
)

play = ft.ElevatedButton(
    "PLAY",
    style=ft.ButtonStyle(
        color="#ffffff",
        bgcolor="#5B0098",
        overlay_color="#0C0C0C",
        shape=ft.RoundedRectangleBorder(radius=3),
        shadow_color="#000000",
        elevation=5,
    ),
    on_click=play_mine,
)

image_promo = ft.Image(
    src='http://127.0.0.1:8090/api/files/lmvwpuuvgk9dan6/79cfxvrsf8j8j6f/promo_RmJczM1Y2F.webp?token=',
    height=50,

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
                controls=[minecraft_title, play, image_promo],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
        ),
    ],
    width=681,
    height=478,
)

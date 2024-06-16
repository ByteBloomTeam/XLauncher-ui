import os
import flet as ft
import minecraft_launcher_lib as mll
from minecraft_launcher.minecraft import list_versions, save_config
import urllib.request

user_windows = os.environ["USERNAME"]
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.xlauncher"

def check_internet():
    try:
        urllib.request.urlopen('http://google.com', timeout=1)
        return True
    except urllib.request.URLError as err: 
        return False

if check_internet():
    versions = list_versions()
else:
    versions = ["No Internet"]

opciones = [ft.dropdown.Option(version) for version in versions]
title = ft.Text('Instalación', font_family='mine_dun', size=30)
pb = ft.ProgressBar(
    width=600, 
    height=10, 
    value=0, 
    color='#5B0098', 
    bgcolor='#1F1F23', 
    border_radius=0
)
dd = ft.Dropdown(
    width=200,
    height=50,
    bgcolor="#343434",
    focused_bgcolor="#343434",
    border=ft.InputBorder.NONE,
    options=opciones,
)

downloadtext = ft.ListView(spacing=5, padding=10, auto_scroll=True)
downloadprogress = ft.ListView(width=50, auto_scroll=True)

def infotext(text):
    downloadtext.controls.clear()
    downloadtext.controls.append(
        ft.Row([ft.Text(text, size=14, color='#ffffff')], alignment="center")
    )
    downloadtext.update()

def infoprog(text):
    downloadprogress.controls.clear()
    downloadprogress.controls.append(
        ft.Row([ft.Text(text, size=14, color='#ffffff')], alignment="center")
    )
    downloadprogress.update()

def install(e):
    if dd.value == "No Internet Connection":
        infotext("No hay conexión a Internet. No se puede instalar.")
    else:
        infotext(install_mine(dd.value))

def printProgressBar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=40,
    fill="●",
    printEnd="",
):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "○" * (length - filledLength)
    pb.value = iteration / total
    pb.update()
    infoprog(f"{prefix} {percent}% {suffix}")

def maximum(max_value, value):
    max_value[0] = value

def install_mine(version):
    max_value = [0]
    callback = {
        "setStatus": lambda text: infotext(text),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value),
    }

    mll.install.install_minecraft_version(
        version, minecraft_directory, callback=callback
    )
    info = mll.utils.generate_test_options()
    save_config(uuid=info["uuid"], version=version)

button_install = ft.ElevatedButton(
    "INSTALAR",
    style=ft.ButtonStyle(
        color="#ffffff",
        bgcolor='#68C90E',
        overlay_color="#447A12",
        shape=ft.RoundedRectangleBorder(radius=0),
    ),
    on_click=lambda _: install(dd.value),
)

install_page = ft.Stack(
    [
        ft.Container(
            content=ft.Column(
                controls=[
                    title,
                    dd,
                    downloadtext,
                    pb,
                    downloadprogress,
                    button_install,
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
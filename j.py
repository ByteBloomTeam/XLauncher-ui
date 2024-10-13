import flet as ft
import minecraft_launcher_lib as mcll
import os
import json
import shutil

# Directorio donde se guardarán los archivos del launcher de Minecraft
minecraft_directory = os.path.expanduser("~/.minecraft_launcher")

# Ruta para el archivo de sesión
session_file = os.path.join(minecraft_directory, "session.json")

# Variables globales para almacenar la información de inicio de sesión
login_data = None

# Función para cargar la sesión desde el archivo si existe
def cargar_sesion(page):
    global login_data
    if os.path.exists(session_file):
        try:
            with open(session_file, 'r') as f:
                login_data = json.load(f)
                resultado.value = f"Sesión cargada: {login_data['name']} (UUID: {login_data['id']})"
        except Exception as e:
            resultado.value = f"Error al cargar la sesión: {e}"
    else:
        resultado.value = "No hay sesión guardada. Inicie sesión con Microsoft o use el modo No-Premium."
    page.update()

# Función para guardar la sesión en un archivo
def guardar_sesion(page):
    global login_data
    try:
        with open(session_file, 'w') as f:
            json.dump(login_data, f)
        resultado.value = f"Sesión guardada para el usuario: {login_data['name']}"
    except Exception as e:
        resultado.value = f"Error al guardar la sesión: {e}"
    page.update()

# Función para manejar el inicio de sesión con Microsoft
def iniciar_sesion_microsoft(event, page):
    global login_data
    try:
        login_data = mcll.account.microsoft_account.login()
        guardar_sesion(page)
    except Exception as e:
        resultado.value = f"Error en la autenticación: {e}"
        page.update()

# Función para aplicar la skin local para usuarios no premium
def aplicar_skin_local(page, username, skin_path):
    try:
        # Crear una carpeta personalizada para la skin en el directorio de Minecraft
        skin_dir = os.path.join(minecraft_directory, f"skins/{username}")
        if not os.path.exists(skin_dir):
            os.makedirs(skin_dir)

        # Copiar la skin a la carpeta de skins del launcher
        skin_destino = os.path.join(skin_dir, "custom_skin.png")
        shutil.copy(skin_path, skin_destino)

        # Crear un archivo JSON para la skin
        skin_json = {
            "skins": [
                {
                    "geometry": "geometry.humanoid.custom",
                    "texture": "custom_skin.png",
                    "geometry_data": {
                        "model": "humanoid"
                    }
                }
            ]
        }

        # Guardar el archivo JSON en la carpeta de skins
        with open(os.path.join(skin_dir, "skin.json"), 'w') as f:
            json.dump(skin_json, f)

        resultado.value = f"Skin local aplicada correctamente para el usuario {username}."
    except Exception as e:
        resultado.value = f"Error al aplicar la skin local: {e}"
    page.update()

# Función para cambiar la skin y lanzar el juego
def cambiar_skin_y_ejecutar(event, page):
    try:
        skin_path = skin_ruta.value
        version = version_minecraft.value
        username = login_data['name'] if login_data else username_field.value

        if not username:
            resultado.value = "Por favor, ingrese un nombre de usuario."
            page.update()
            return

        if skin_path and version:
            if login_data:
                # Modo premium: Cambiar la skin usando la API de Minecraft
                mcll.utils.change_skin(login_data['name'], skin_path)
                resultado.value = f"Skin aplicada correctamente para el usuario premium: {login_data['name']}."
            else:
                # Modo no premium: Aplicar la skin localmente
                aplicar_skin_local(page, username, skin_path)
            
            # Preparar las opciones de lanzamiento
            options = {
                "username": username,
                "uuid": login_data["id"] if login_data else username,  # Usamos el username como UUID si es no premium
                "token": login_data["access_token"] if login_data else "",  # Dejar vacío para no premium
            }

            # Ejecutar Minecraft con la versión seleccionada
            mcll.launch(minecraft_directory, options)

            resultado.value += f"\nMinecraft se está ejecutando con la versión {version}."
        else:
            resultado.value = "Por favor, complete los campos (ruta de skin y versión de Minecraft)."
    except Exception as e:
        resultado.value = f"Error al cambiar la skin o ejecutar Minecraft: {e}"

    page.update()

# Creación de la interfaz con Flet
def main(page: ft.Page):
    page.title = "Minecraft Skin Changer & Launcher"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    global skin_ruta, version_minecraft, resultado, username_field
    
    # Botón para iniciar sesión con Microsoft
    boton_login = ft.ElevatedButton("Iniciar sesión con Microsoft", on_click=lambda e: iniciar_sesion_microsoft(e, page))
    
    # Campo para el nombre de usuario (para usuarios no premium)
    username_field = ft.TextField(label="Nombre de Usuario (Modo No-Premium)", width=400)
    
    # Entrada para la ruta de la skin
    skin_ruta = ft.TextField(label="Ruta de la Skin", width=400)
    
    # Entrada para seleccionar la versión de Minecraft
    version_minecraft = ft.TextField(label="Versión de Minecraft (e.g. 1.16.5)", width=400)
    
    # Botón para aplicar la skin y lanzar el juego
    boton_aplicar = ft.ElevatedButton("Aplicar Skin y Ejecutar Minecraft", on_click=lambda e: cambiar_skin_y_ejecutar(e, page))
    
    # Campo de resultado para mostrar el mensaje
    resultado = ft.Text("")
    
    # Cargar sesión automáticamente si existe
    cargar_sesion(page)

    # Agregar todos los elementos a la página
    page.add(boton_login, username_field, skin_ruta, version_minecraft, boton_aplicar, resultado)

# Ejecutar la app Flet
ft.app(target=main)

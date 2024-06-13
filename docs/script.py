import requests

# Reemplaza 'usuario' y 'repositorio' con los tuyos
url = "https://api.github.com/repos/usuario/repositorio/contributors"

# Realiza la solicitud a la API de GitHub
response = requests.get(url)
contributors = response.json()

# Abre el archivo README.md o crea uno si no existe
with open('README.md', 'a') as readme:
    # Escribe la etiqueta de inicio
    readme.write('<--- Inicio --->\n')
    
    # Escribe las imágenes de perfil de los contribuyentes en el README
    for contributor in contributors:
        profile_image_url = contributor['avatar_url']
        username = contributor['login']
        readme.write(f"!{username}\n")
    
    # Escribe la etiqueta de fin
    readme.write('<--- Fin --->\n')

print("Las fotos de perfil se han agregado al README entre las etiquetas especificadas.")

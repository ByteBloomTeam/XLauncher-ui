<div align="center">
    <img src="docs/XLauncher LogoX.webp" alt="Launcher de Minecraft" height="250">
</div>

# Minecraft Launcher

![1711569832079](docs/XLauncher-UI.png "Interfaz del XLauncher")

> Launcher de minecraft que hice para un video de YouTube

![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/KeimaSenpai/XLauncher-ui/total?style=for-the-badge&label=Download&color=%23756AB6)

## 🔩Instalación

- Clonar repositorio

```console
git clone https://github.com/KeimaSenpai/Script-launcher-Minecraft.git
```

- Crear entorno de desarrollo

```console
pip install virtualenv
virtualenv env
```

- Instalar dependencias

```console
pip install -r requirements.txt
```

🔩Instalación para los usuarios de Cuba

> Para que no gasten megas en la instalacion del paquete pueden usar este comando
> Solo funciona para CUBA este comando

```console
python -m pip install -r requirements.txt --index-url http://nexus.prod.uci.cu/repository/pypi-proxy/simple/ --trusted-host nexus.prod.uci.cu
```

### 📦Para empaquetar

```console
flet pack  main.py --name XLauncher --onedir --icon icon_windows.ico --product-name XLauncher --add-data "assets;assets" --product-version "1.0.0" --copyright "Copyright (c) 2024 ByteBloom"
```

> Link de la documentación [LINK](https://minecraft-launcher-lib.readthedocs.io/en/stable/)

## 📺Video de YouTube

> Recuerda dejar Like y no dejes de suscribirte al canal 👍
> [CREA TU PROPIO LAUNCHER de MINECRAFT](https://youtu.be/5FmjSubDRyw?si=9brYY9OnENftZgft)

## Personas que hicieron este proyecto posible
[![Contributors](https://contrib.rocks/image?repo=ByteBloomTeam/XLauncher-ui)](https://github.com/ByteBloomTeam/XLauncher-ui/graphs/contributors)

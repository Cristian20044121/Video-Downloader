# Video Downloader App

Este es un proyecto de una **aplicación web** desarrollada en Python utilizando **Flask**. La aplicación permite descargar videos de **YouTube** en diferentes resoluciones y formatos de audio.

## Descripción del Código

El archivo `app.py` contiene el código principal de la aplicación. Aquí hay una descripción de las principales funciones y rutas:

- **`download_video(url, output_path)`**: Esta función utiliza la biblioteca `pytube` para descargar el video de YouTube con la URL proporcionada en la ubicación de salida especificada.

- **`download_audio(url, output_path)`**: Similar a la función anterior, esta función descarga solo el audio del video de YouTube.

- **`/` (Ruta de Inicio)**: Esta ruta renderiza la plantilla `index.html`, que sirve como página de inicio de la aplicación.

- **`/download` (Ruta de Descarga)**: Esta ruta maneja las solicitudes POST para descargar videos de YouTube. Primero verifica si se proporciona una URL válida, luego intenta descargar el video y el audio en rutas diferentes. Si hay algún error durante la descarga, se muestra un mensaje de error.

## Conexión con HTML y CSS

La aplicación se conecta con **HTML** y **CSS** a través de las plantillas `index.html`, `download_error.html` y `download_complete.html`. Estas plantillas proporcionan la interfaz de usuario para la aplicación, permitiendo al usuario ingresar la URL del video y mostrando mensajes de error o éxito después de la descarga.
<<<<<<< HEAD

## Ejecutar la Aplicación

Para ejecutar la aplicación, simplemente ejecute el archivo `app.py`. La aplicación se ejecutará en modo de depuración, lo que facilitará el desarrollo y la depuración.

```bash
python app.py
```
=======

## Ejecutar la Aplicación

Para ejecutar la aplicación, simplemente ejecute el archivo `app.py`. La aplicación se ejecutará en modo de depuración, lo que facilitará el desarrollo y la depuración.

```bash
python app.py

>>>>>>> 7db67980597b2eca1f8ff9541c22efe8b3850931

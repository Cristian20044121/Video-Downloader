from flask import Flask, render_template, request
from pytube import YouTube
import os
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Configurar el nivel de registro
app.logger.setLevel(logging.DEBUG)

# Configurar un manejador de registros adicional para escribir en un archivo
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
    except Exception as e:
        app.logger.error(f"Error en la descarga de video: {e}")
        raise

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path)
    except Exception as e:
        app.logger.error(f"Error en la descarga de audio: {e}")
        raise

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            return render_template("download_error.html", error="No se proporcionó una URL.")

        try:
            # Descargar video y audio en rutas diferentes
            video_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'video')
            audio_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'audio')
            
            download_video(url, video_path)
            download_audio(url, audio_path)
            return render_template("download_complete.html")
        except Exception as e:
            error_message = f"Error al descargar el video o audio: {e}"
            app.logger.error(error_message)
            return render_template("download_error.html", error=error_message)

    # Si la solicitud no es POST, mostrar un mensaje de error
    return render_template("download_error.html", error="Se esperaba una solicitud POST.")

if __name__ == "__main__":
    # Cambiar la dirección de escucha a 0.0.0.0 para que sea accesible desde cualquier dirección IP
    app.run(host='0.0.0.0', debug=True)

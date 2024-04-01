# Archivo: app.py

from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)

def download_audio(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path)

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
            print(error_message)
            return render_template("download_error.html", error=error_message)

    # Si la solicitud no es POST, mostrar un mensaje de error
    return render_template("download_error.html", error="Se esperaba una solicitud POST.")

if __name__ == "__main__":
    app.run(debug=True)

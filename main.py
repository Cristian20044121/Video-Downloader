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

@app.route("/download", methods=["GET", "POST"])
def download():
    if request.method == "POST":
        url = request.form["url"]
        try:
            download_video(url, os.path.join(os.path.expanduser('~'), 'Downloads'))
            download_audio(url, os.path.join(os.path.expanduser('~'), 'Downloads'))
            return render_template("download_complete.html")
        except Exception as e:
            error_message = f"Error al descargar el video o audio: {e}"
            print(error_message)
            return render_template("download_error.html", error=error_message)
    else:
        error_message = "Error: Se esperaba una solicitud POST."
        print(error_message)
        return render_template("download_error.html", error=error_message)

if __name__ == "__main__":
    # Aumenta el tiempo de espera del servidor a 120 segundos
    app.run(debug=True, timeout=120)

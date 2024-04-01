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
            print(f"Error al descargar el video o audio: {e}")
            return render_template("download_error.html", error=str(e))
    else:
        print("Error: Se esperaba una solicitud POST.")
        return render_template("download_error.html", error="Se esperaba una solicitud POST.")

if __name__ == "__main__":
    # Ajustar el tiempo de espera del trabajador a 60 segundos (por defecto es 30)
    app.run(debug=True, port=5000, host='0.0.0.0', threaded=True, request_timeout=60)

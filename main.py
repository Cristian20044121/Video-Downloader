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
        download_video(url, os.path.join(os.path.expanduser('~'), 'Downloads'))
        download_audio(url, os.path.join(os.path.expanduser('~'), 'Downloads'))
        return "Tu descarga ha sido completada! Gracias por estar aquí."
    else:
        # Manejar aquí el caso en el que se realiza una solicitud GET a /download
        print("error en la descarga")
        pass

if __name__ == "__main__":
    app.run(debug=True)

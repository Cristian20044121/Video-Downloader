from flask import Flask, render_template, request
from pytube import YouTube
from pytube.exceptions import PytubeError
import os

app = Flask(__name__)

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        return True
    except PytubeError:
        print("Error: la URL proporcionada no es válida.")
        return False
    except Exception as e:
        print("Error en la descarga de video:", e)
        return False

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path)
        return True
    except PytubeError:
        print("Error: la URL proporcionada no es válida.")
        return False
    except Exception as e:
        print("Error en la descarga de audio:", e)
        return False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    if request.method == "POST":
        url = request.form["url"]
        video_success = download_video(url, os.path.join(os.path.expanduser('~'), 'Downloads'))
        audio_success = download_audio(url, os.path.join(os.path.expanduser('~'), 'Downloads'))
        if video_success and audio_success:
            return render_template("download_complete.html")
        else:
            return render_template("download_error.html")
    else:
        print("Error: Se esperaba una solicitud POST.")
        return render_template("download_error.html")

if __name__ == "__main__":
    app.run(debug=True)

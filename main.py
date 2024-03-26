import os
from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        return True
    except Exception as e:
        print("Error en la descarga de video:", e)
        return False

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path)
        return True
    except Exception as e:
        print("Error en la descarga de audio:", e)
        return False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["GET", "POST"])
def download():
    if request.method == "POST":
        url = request.form["url"]
        # Define la ruta de descarga en función del tipo de dispositivo
        if request.user_agent.platform in ['android', 'iphone']:
            download_dir = os.path.join(os.path.expanduser('~'), '/storage/emulated/0/Download')
        else:
            download_dir = os.path.join(os.path.expanduser('~'), '/storage/emulated/0/Download')
        video_success = download_video(url, download_dir)
        audio_success = download_audio(url, download_dir)
        if video_success and audio_success:
            return render_template("download_complete.html")
        else:
            return render_template("download_error.html")
    else:
        return "Método no permitido"

if __name__ == "__main__":
    app.run(debug=True)

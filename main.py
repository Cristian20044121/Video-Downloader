from flask import Flask, render_template, request
from pytube import YouTube
import os
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def download_video_task(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)

@celery.task
def download_audio_task(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    if request.method == "POST":
        url = request.form["url"]
        output_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        video_task = download_video_task.delay(url, output_path)
        audio_task = download_audio_task.delay(url, output_path)
        return render_template("download_in_progress.html", video_task_id=video_task.id, audio_task_id=audio_task.id)
    else:
        return render_template("download_error.html", error="Se esperaba una solicitud POST.")

if __name__ == "__main__":
    app.run(debug=True)

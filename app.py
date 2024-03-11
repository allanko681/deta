from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def route():
    return render_template('r.html')

@app.route('/d', methods = ['POST'])
def d():
    url = request.form['url']
    video = YouTube(url)
    stream = video.streams.filter(only_audio=True).first()
    filename = stream.default_filename
    filepath = f"/opt/render/project/src/{filename}.mp3"
    stream.download(filepath)
    return send_file(filepath, as_attachment=True)
if __name__ == '__main__':
    app.run

from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

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
    filepath = f"/opt/render/project/src/{filename}"
    stream.download(filepath)
    
    # Cambiar la extensión del archivo a mp3 si no lo es ya
    if not filepath.endswith(".mp3"):
        mp3_filepath = f"{filepath}.mp3"
        os.rename(filepath, mp3_filepath)
        filepath = mp3_filepath
    
    return send_file(filepath, as_attachment=True)
if __name__ == '__main__':
    app.run

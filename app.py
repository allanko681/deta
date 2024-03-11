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
    extension = stream.extension
    filepath = f"/opt/render/project/src/{filename}"
    stream.download(filepath)
    
    # Cambiar la extensión del archivo a mp3
    new_filepath = f"{filepath.rsplit('.', 1)[0]}.mp3"
    os.rename(filepath, new_filepath)
if __name__ == '__main__':
    app.run

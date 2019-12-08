import os
import video_input as vi
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'mp4'}
UPLOAD_FOLDER = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        # if user does not select file, browser also
        # submit an empty part without filename
        file = request.files['file']
        if file.filename == '':
            # flash('No selected file')
            return 'No files uploaded!'
            # return render_template('login.html')
        if file and allowed_file(file.filename):
            file.filename = 'userInput.mp4'
            file.save(secure_filename(file.filename))
            vi.video_input("userInput")
            return render_template('login.html')
            # return 'File uploaded successfully...'
        else:
            return "Wrong file type! Please re-upload a different file."


# @app.route('/')
# def student():
#    return render_template('student.html')

@app.route('/upload')
def upload_file():
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)


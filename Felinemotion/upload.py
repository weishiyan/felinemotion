import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'mp4'}
UPLOAD_FOLDER = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')
def upload_file():
    return render_template('upload.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return render_template('upload.html')
        # if user does not select file, browser also
        # submit an empty part without filename
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('upload.html')
        # if file and allowed_file(file.filename):
        file.save(secure_filename(file.filename))
    return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
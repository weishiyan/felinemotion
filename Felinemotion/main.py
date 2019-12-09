import video_input as vi
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import audio_input
import image_output
import svm
import random_pick_3

"""This is the main script that run the modules and connect to the user interface"""

"""These TODOs are what needs to be done to fully run the main script!!!"""
# TODO: everyone's functions will receive input and export output into the directory, no returning variables
# TODO: test run your parts BEFORE putting it in the main script, make sure the variable names match


ALLOWED_EXTENSIONS = {'mp4'}
UPLOAD_FOLDER = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    """Check if the file has the required extension of types"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    """Process video input from the user interface and proceed to image selection web page"""
    if request.method == 'POST':
        # if user does not select file, browser also
        # submit an empty part without filename
        file = request.files['file']
        if file.filename == '':
            # flash('No selected file')
            return 'No files uploaded!'

        if file and allowed_file(file.filename):
            # rename the user input video and save it
            file.filename = 'userInput.mp4'
            file.save(secure_filename(file.filename))
            # extract audio data and image frames from input
            vi.video_input("userInput")
            audio_input.audio_input('userData/userInput.wav')
            random_pick_3.pick_three('userData/catFaces', 'userData/cat3Faces')
            # proceed to image selection
            return render_template('image.html')
        else:
            # throw warning when wrong file type uploaded
            return "Wrong file type! Please re-upload a different file."


@app.route('/a')
def img1():
    """This function received the selected image, convert it to csv and run SVM analysis"""
    image_output.image_output('userData/', 'user1.JPG')
    svm.csv_merge('userData/selected_image.csv', 'userData/audio_test.csv')
    result = svm.classification('userData/user_csv.csv')
    return 'Your cat is ' + str(result[0]) + '!'


@app.route('/b')
def img2():
    """This function received the selected image, convert it to csv and run SVM analysis"""
    image_output.image_output('userData/', 'user2.JPG')
    svm.csv_merge('userData/selected_image.csv', 'userData/audio_test.csv')
    result = svm.classification('userData/user_csv.csv')
    return 'Your cat is ' + str(result[0]) + '!'


@app.route('/c')
def img3():
    """This function received the selected image, convert it to csv and run SVM analysis"""
    image_output.image_output('userData/', 'user3.JPG')
    svm.csv_merge('userData/selected_image.csv', 'userData/audio_test.csv')
    result = svm.classification('userData/user_csv.csv')
    return 'Your cat is ' + str(result[0]) + '!'


@app.route('/upload')
def upload_file():
    return render_template('Felinemotion.html')


if __name__ == '__main__':
    app.run(debug=True)


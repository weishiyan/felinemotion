import os
import cv2
import numpy as np
import moviepy.editor as mp

""" This script receive a mp4 file in the same directory as input
    output will be a folder of extracted frames and a wav file for audio
    that has the same name as the input"""


def video_input(name):

    # Extract the audio into wav file
    name = name - ".mp4"
    audioClip = mp.AudioFileClip(name + ".mp4")
    audioClip.write_audiofile(name + ".wav")

    # Create a VideoCapture object
    cam = cv2.VideoCapture(name + ".mp4")

    try:
        # creating a folder named data
        if not os.path.exists(name):
            os.makedirs(name)

        # if not created then raise error
    except OSError:
        print('Error: Creating directory of frames')

    # Check if camera opened successfully
    if (cam.isOpened() == False):
        print("Unable to read camera feed")

    # frame
    currentframe = 0
    while (True):

        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            frameName = './' + name + '/frame' + str(currentframe) + '.jpg'
            # print('Creating...' + frameName)

            # writing the extracted images
            cv2.imwrite(frameName, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # When everything done, release the video capture and video write objects
    # cam.release()

    # Closes all the frames
    cv2.destroyAllWindows()
""" This module receive a mp4 file in the same directory as input
    output will be a folder of extracted frames and a wav file for audio
    that has the same name as the input
        Input: video name that in the same directory
        Output: exported WAV file and a folder of image frames"""

import os
import moviepy.editor as mp
import cv2


def video_input(name):
    """Extract audio file and images frame from user video"""
    # Extract the audio into wav file
    audio = mp.AudioFileClip(name + ".mp4")
    audio.write_audiofile('./userData/' + name + ".wav")

    # Create a VideoCapture object
    cam = cv2.VideoCapture(name + ".mp4")

    # try:
    #     # creating a folder named data
    #     if not os.path.exists("userData/frames"):
    #         os.makedirs("userData/frames")
    #
    #     # if not created then raise error
    # except OSError:
    #     print('Error: Creating directory of frames')
    #
    # # Check if camera opened successfully
    # if cam.isOpened() is False:
    #     print("Unable to read camera feed")

    # frame
    current_frame = 0
    while True:

        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            frame_name = './' + 'userData/frames' + '/frame' + str(current_frame) + '.jpg'
            # print('Creating...' + frameName)

            # writing the extracted images
            cv2.imwrite(frame_name, frame)

            # increasing counter so that it will
            # show how many frames are created
            current_frame += 1
        else:
            break

    # When everything done, release the video capture and video write objects
    # cam.release()

    # Closes all the frames
    cv2.destroyAllWindows()

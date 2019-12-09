"""
Analyze cat image from video frames
Import: video frames
Ouput: images with cat face
"""
import os
import cv2
import clear_folder

def cat_detect(pathstring, detectorstring):
    """
    Import video frames
    Detect cat face from CascadeClassifier
    create 'catFace' folder for saving cat face images
    save images
    """
    # clear_folder
    path = pathstring
    #Video Frame file path
    #path = 'e:\\2019fall\\CSE583\\FellinEmotion\\cat-face-detector\\images\\'
    detect = detectorstring
    #CascadeClassifier (haarcascade_frontalcatface.xml) file path
    #detect = 'E:\\2019fall\CSE583\FellinEmotion\cat-face-detector\haarcascade_frontalcatface.xml'

    files_out = []
    
    # import raw images
    for root, directories, files in os.walk(path):
        for file in files:
            files_out.append(os.path.join(root, file))
    
    # create folder
    dir_name = 'userData/catFaces'
    os.mkdir(dir_name)
    # Cat face detector
    for files in files_out:
        img = cv2.imread(files)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detector = cv2.CascadeClassifier(detect)
        rects = detector.detectMultiScale(gray, scaleFactor=1.3,
                                          minNeighbors=10, minSize=(75, 75))
        if type(rects) != tuple:
            # catFaces=[]
            for (i, (xloc, yloc, width, hight)) in enumerate(rects):
                mid_x = (2*xloc + width)/2
                mid_y = (2*yloc + hight)/2
                mid_x = mid_x.astype(int)
                mid_y = mid_y.astype(int)
                cv2.rectangle(img, (mid_x - 100, mid_y - 100),
                              (mid_x + 100, mid_y + 100), (0, 0, 255), 2)
                cv2.putText(img, "Cat #{}".format(i + 1),
                            (mid_x, mid_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
            gray_size = gray.shape
            x_rang = gray_size[0] - 100
            y_rang = gray_size[1] - 100
            if mid_x <= x_rang:
                if mid_x >= 100:
                    if mid_y <= y_rang:
                        if mid_y >= 100:
                            for (i, (xloc, yloc, width, hight)) in enumerate(rects):
                                face = gray[mid_y - 100:mid_y + 100, mid_x - 100:mid_x + 100]
                                # save images
                                base = os.path.basename(files)
                                cv2.imwrite(os.path.join('userData/catFaces/', base), face)
                                
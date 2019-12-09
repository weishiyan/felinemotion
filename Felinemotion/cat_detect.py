# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:00:55 2019

@author: Jerry
"""
import os
import numpy as np
import csv
from numpy import asarray
from numpy import savetxt
def cat_detect(pathstring, path2string, detectorstring):
    """
    test
    """
    path = pathstring
    #Video Frame file path
    #path = 'e:\\2019fall\\CSE583\\FellinEmotion\\cat-face-detector\\images\\'
    path2 = path2string
    #Images with cat face file save path
    #path2 = 'e:\\2019fall\\CSE583\\FellinEmotion\\cat-face-detector\\image_select\\'
    detect = detectorstring
    #CascadeClassifier (haarcascade_frontalcatface.xml) file path
    #detect = 'E:\\2019fall\CSE583\FellinEmotion\cat-face-detector\haarcascade_frontalcatface.xml'
    files_out = []
    # r=root, d=directories, f = files
    for root, directories, files in os.walk(path):
        for file in files:
            files_out.append(os.path.join(root, file))
    for files in files_out:
        img = cv2.imread(f)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detector = cv2.CascadeClassifier(detect)
        rects = detector.detectMultiScale(gray, scaleFactor=1.3,
        minNeighbors=10, minSize=(75, 75))
        if type(rects) != tuple:
            rows=rects.shape[0]
            catFaces=[]
            for (i, (x, y, w, h)) in enumerate(rects):
                mid_x = (2*x + w)/2
                mid_y = (2*y + h)/2
                mid_x = mid_x.astype(int)
                mid_y = mid_y.astype(int)
                cv2.rectangle(img, (mid_x - 100,mid_y - 100), (mid_x + 100, mid_y + 100), (0, 0, 255), 2)
                cv2.putText(img, "Cat #{}".format(i + 1), (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255))
                            
            for (i, (x, y, w, h)) in enumerate(rects):
                face=gray[mid_y - 100:mid_y + 100,mid_x - 100:mid_x + 100]
                catFaces.append(face)
                base = os.path.basename(f)
                cv2.imwrite(os.path.join(path2, base), face)

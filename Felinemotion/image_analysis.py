
import cv2
import os
import numpy as np
import csv
from numpy import asarray
from numpy import savetxt

def cat_detect(pathString,  detectorString):

	path = pathString
	#Video Frame file path
	#path = 'e:\\2019fall\\CSE583\\FellinEmotion\\cat-face-detector\\images\\'
	detect = detectorString
	#CascadeClassifier (haarcascade_frontalcatface.xml) file path
	#detect = 'E:\\2019fall\CSE583\FellinEmotion\cat-face-detector\haarcascade_frontalcatface.xml'
	
	files_out = []
	# r=root, d=directories, f = files
	for root, directories, files in os.walk(path):
		for file in files:
			files_out.append(os.path.join(root, file))
	dirName = 'catFaces'
	os.mkdir(dirName)
	for files in files_out:
		img = cv2.imread(files)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		detector = cv2.CascadeClassifier(detect)
		rects = detector.detectMultiScale(gray, scaleFactor=1.3,
		minNeighbors=10, minSize=(75, 75))
		if type(rects) != tuple:
			rows=rects.shape[0]
			catFaces=[]
			for (i, (x, y, w, h)) in enumerate(rects):
				mx = (2*x + w)/2
				my = (2*y + h)/2
				mx = mx.astype(int)
				my = my.astype(int)
				cv2.rectangle(img, (mx - 100,my - 100), (mx + 100, my + 100), (0, 0, 255), 2)
				cv2.putText(img, "Cat #{}".format(i + 1), (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
			for (i, (x, y, w, h)) in enumerate(rects):
				face=gray[my - 100:my + 100,mx - 100:mx + 100]
				catFaces.append(face)
				base = os.path.basename(files)
				cv2.imwrite(os.path.join('catFaces/', base), face)


import cv2
import os
import numpy as np
import csv
from numpy import asarray
from numpy import savetxt
import clear_folder


def cat_detect(pathString,  detectorString):

	# clear_folder
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
	dirName = 'userData/catFaces'
	os.mkdir(dirName)
	for files in files_out:
		img = cv2.imread(files)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		detector = cv2.CascadeClassifier(detect)
		rects = detector.detectMultiScale(gray, scaleFactor=1.3,
		minNeighbors=10, minSize=(75, 75))
		if type(rects) != tuple:
			rows=rects.shape[0]
			# catFaces=[]
			for (i, (x, y, w, h)) in enumerate(rects):
				mid_x = (2*x + w)/2
				mid_y = (2*y + h)/2
				mid_x = mid_x.astype(int)
				mid_y = mid_y.astype(int)
				cv2.rectangle(img, (mid_x - 100,mid_y - 100), (mid_x + 100, mid_y + 100), (0, 0, 255), 2)
				cv2.putText(img, "Cat #{}".format(i + 1), (mid_x, mid_y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
			gray_size = gray.shape
			x_rang = gray_size[0] - 100
			y_rang = gray_size[1] - 100
			if mid_x <= x_rang:
				if 100 <= mid_x:
					if mid_y <= y_rang:
						if 100 <= mid_y:
							for (i, (x, y, w, h)) in enumerate(rects):
								face=gray[mid_y - 100:mid_y + 100,mid_x - 100:mid_x + 100]
								# catFaces.append(face)
								base = os.path.basename(files)
								cv2.imwrite(os.path.join('userData/catFaces/', base), face)
								# cv2.imwrite('userData/catFaces/' + base, face)

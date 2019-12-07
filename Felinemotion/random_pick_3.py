import cv2
import os
import numpy as np
import random
import csv

from numpy import asarray
from numpy import savetxt

def pick_three(path2String, outputString):
		path2 = path2String
		#Images with cat face file save path
		#path2 = 'e:\\2019fall\\CSE583\\FellinEmotion\\cat-face-detector\\image_select\\'
		output = outputString
		#Images with cat face file save path
		#output = 'e:\\2019fall\\CSE583\\FellinEmotion\\cat-face-detector\\image_output\\'
	files = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path2):
		for file in f:
			files.append(os.path.join(r, file))
	k = random.sample(files, 3)
	pick1 = k[1]
	pick2 = k[2]
	pick3 = k[0]
	pick1_1 = cv2.imread(pick1)
	pick1_2 = cv2.imread(pick2)
	pick1_3 = cv2.imread(pick3)
	base1 = os.path.basename(pick1)
	base2 = os.path.basename(pick2)
	base3 = os.path.basename(pick3)
	cv2.imwrite(os.path.join(output, base1), pick1_1)
	cv2.imwrite(os.path.join(output, base2), pick1_2)
	cv2.imwrite(os.path.join(output, base3), pick1_3)

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:00:55 2019

@author: Jerry
"""
import os
import random
import cv2
def pick_three(path2string, outputstring):
	"""
	test
	"""
	# dir = "userData/"
	path2 = path2string
	output = outputstring
	files_out = []
	# r=root, d=directories, f = files
	for root, directories, files in os.walk(path2):
		for file in files:
			files_out.append(os.path.join(root, file))
	rand = random.sample(files_out, 3)
	pick1 = rand[1]
	pick2 = rand[2]
	pick3 = rand[0]
	pick1_1 = cv2.imread(pick1)
	pick1_2 = cv2.imread(pick2)
	pick1_3 = cv2.imread(pick3)
	base1 = 'user1.jpg'
	base2 = 'user2.jpg'
	base3 = 'user3.jpg'
	cv2.imwrite(os.path.join(output, base1), pick1_1)
	cv2.imwrite(os.path.join(output, base2), pick1_2)
	cv2.imwrite(os.path.join(output, base3), pick1_3)
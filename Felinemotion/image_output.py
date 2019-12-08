# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:00:55 2019

@author: Jerry
"""

import cv2
import os
import numpy as np
import csv
import pandas as pd
#load selected image
def image_output(image2String, csvString):
	image_loc = image2String
    #image path
    #path = 'E:\\2019fall\CSE583\FellinEmotion\cat-face-detector\image_select\happy_02_YG.JPG'
	csv_loc = csvString
    #'E:\\2019fall\CSE583\FellinEmotion\cat-face-detector\image_output\data.csv'
    
    
	img = cv2.imread(image_loc,0)
	A = np.asarray(img).reshape(-1)
	Q = []
	n=400
	for i in range(0,n):
		j = i*100 + 1
		B = sum (A [j:100+j])
		C = B / 100
		Q.append(C)
	df = pd.DataFrame(Q, columns = ['CatID'])
#QQ = np.transpose(Q2)
	df.to_csv(csv_loc)

#cv2.imshow('image',img)
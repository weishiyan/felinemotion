import os

import matplotlib.pyplot as plt
import librosa
import numpy as np
import pandas as pd

from numpy import asarray
from numpy import savetxt
from os.path import join
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

def convert_mel_one(sound):
    SR = 16000
    src, sr = librosa.load(sound, sr=SR, mono=True)
    len_second = 3.0 # 3 seconds
    src = src[:int(sr*len_second)] # crop first 3 seconds
    if len(src) < int(sr*len_second):
        N = int(sr*len_second) - len(src)
        src = np.pad(src, (0, N), 'constant')
    src_mel = librosa.feature.melspectrogram(y=src, sr=sr)
    return src_mel.flatten()

def save_csv_raw(sound_folder):
    files_list = os.listdir(sound_folder)    
    csv_file = np.zeros(12032)
    classifier = ['catID']
    for i in files_list:
        if i.endswith('.wav'):
            converted = convert_mel_one(join(sound_folder,i))
            classifier_itr = i[:-4]
            classifier = np.append(classifier,classifier_itr)
            csv_file = np.vstack((csv_file,converted))
    savetxt(sound_folder+'/raw.csv',csv_file,delimiter=",")
    return classifier

def add_label():
    alpha_list = [] 
    alpha = 'a'
    for i in range(0, 20): 
        alpha_list.append(alpha) 
        alpha = chr(ord(alpha) + 1)
    return alpha_list




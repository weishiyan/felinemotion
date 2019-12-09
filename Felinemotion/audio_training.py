'''
This module contains some essential functions for sound analysis
All modules in this software need to import this module for proper usage

'''

import os
from os.path import join

import numpy as np
import librosa
from numpy import savetxt

def convert_mel_one(sound):
    '''
    This function convert one single wav file to numerical data using mel-spectrogram analysis
    Return 1D array 
    '''
    src, s_rate = librosa.load(sound, sr=16000, mono=True)
    len_second = 3.0 # 3 seconds
    src = src[:int(s_rate*len_second)] # crop first 3 seconds
    if len(src) < int(s_rate*len_second):
        num_s = int(s_rate*len_second) - len(src)
        src = np.pad(src, (0, num_s), 'constant')
    src_mel = librosa.feature.melspectrogram(y=src, sr=s_rate)
    return src_mel.flatten()

def save_csv_raw(sound_folder):
    '''
    This function convert batch wav files in one folder and save all files in an N-demensional array csv file
    The audio_raw.csv file will be save in the same folder as the raw wav files
    The function return the label of each wav file
    '''
    files_list = os.listdir(sound_folder)
    csv_file = np.zeros(12032)
    classifier = ['catID']
    for i in files_list:
        if i.endswith('.wav'):
            converted = convert_mel_one(join(sound_folder, i))
            classifier_itr = i[:-4]
            classifier = np.append(classifier, classifier_itr)
            csv_file = np.vstack((csv_file, converted))
    savetxt('audio_raw.csv', csv_file, delimiter=",")
    savetxt(sound_folder+'/audio_raw.csv', csv_file, delimiter=",")
    return classifier

def add_label():
    '''
    This function generate 20 alphabets as feature names for SVM
    '''
    alpha_list = []
    alpha = 'a'
    for i in range(0, 20):
        alpha_list.append(alpha)
        alpha = chr(ord(alpha) + 1)
    return alpha_list

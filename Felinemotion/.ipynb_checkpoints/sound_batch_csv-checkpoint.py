import os

import matplotlib.pyplot as plt
import librosa
import numpy as np
import pandas as pd

from numpy import asarray
from numpy import savetxt
from os.path import join



def save_csv_raw(sound_folder):
    files_list = os.listdir(sound_folder)    
    csv_file = np.zeros(12032)
    classifier = np.zeros(0)
    for i in files_list:
        if i.endswith('.wav'):
            converted = convert_mel_one(join(sound_folder,i))
            classifier_itr = i[:-4]
            classifier = np.append(classifier,classifier_itr)
            csv_file = np.vstack((csv_file,converted))
            
    classifier = classifier[np.newaxis].T
    savetxt(sound_folder+'/raw.csv',csv_file,delimiter=",")
    return classifier
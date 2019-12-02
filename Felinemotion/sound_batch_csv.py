import os

import matplotlib.pyplot as plt
import librosa
import numpy as np
import pandas as pd

from numpy import asarray
from numpy import savetxt
from os.path import join

def save_csv(sound_folder):
    files_list = os.listdir(sound_folder)    
    csv_file = convert_mel_one(join(sound_folder,files_list[3]))
    del files_list[3]
    for i in files_list:
        if i.endswith('.wav'):
            converted = convert_mel_one(join(sound_folder,i))
            csv_file = np.vstack((csv_file,converted))
    savetxt(sound_folder+'/raw.csv',csv_file,delimiter=",")
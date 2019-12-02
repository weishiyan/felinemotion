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
    temp = convert_mel_one(join(sound_folder,files_list[0]))
    del files_list[0]
    csv_file = temp.flatten()
    for i in files_list:
        converted = convert_mel_one(join(sound_folder,i))
        flattened = converted.flatten()
        csv_file = np.vstack((csv_file,flattened))
    
    savetxt(sound_folder+'/raw.csv',csv_file,delimiter=",")
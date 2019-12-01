import os

import matplotlib.pyplot as plt
import librosa
import numpy as np
import pandas as pd

from numpy import asarray
from numpy import savetxt
from os.path import join

def save_csv(sound_folder,csv_folder):
    files_list = os.listdir(sound_folder)
    for i in files_list:
        converted = convert_mel_one(join(sound_folder,i))
        i = i.replace('.wav', '.csv')
        savetxt(join(csv_folder,i), converted)
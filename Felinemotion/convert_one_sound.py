import os

import matplotlib.pyplot as plt
import librosa
import numpy as np
import pandas as pd

from numpy import asarray
from numpy import savetxt
from os.path import join

def convert_mel_one(sound):
    SR = 16000
    src, sr = librosa.load(sound, sr=SR, mono=True)
    len_second = 3.0 # 3 seconds
    src = src[:int(sr*len_second)] # crop first 3 seconds
    src_mel = librosa.feature.melspectrogram(y=src, sr=sr)
    return src_mel

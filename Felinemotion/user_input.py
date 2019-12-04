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

import sound_to_csv

#### user input sound and dimension reduction

user_sound  = sound_to_csv.convert_mel_one('user_input.wav')
X_features.loc[len(X_features)] = user_sound

scaler = StandardScaler()
X_features_scaled = scaler.fit_transform(X_features)
pca = PCA(n_components=20)
pca.fit(X_features_scaled)
x_reduced = pca.transform(X_features_scaled)

alpha_list = sound_to_csv.add_label()
user_output = pd.DataFrame(np.vstack((alpha_list,x_reduced[-1])))
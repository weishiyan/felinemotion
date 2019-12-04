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

#### create data for model
folder_name = '../data/vid/trainingSet/raw'
classifier = sound_to_csv.save_csv_raw(folder_name)
X_features = pd.read_csv('../data/vid/trainingSet/raw/raw.csv')


scaler = StandardScaler()
X_features_scaled = scaler.fit_transform(X_features)
pca = PCA(n_components=20)
pca.fit(X_features_scaled)
x_reduced = pca.transform(X_features_scaled)

alpha_list = sound_to_csv.add_label()
full = pd.DataFrame(np.append(classifier[np.newaxis].T, np.vstack((alpha_list,x_reduced)),1))
full.to_csv (r'../data/vid/trainingSet/raw/full.csv', index = None, header=False)


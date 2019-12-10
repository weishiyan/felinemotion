'''
This module contains a function that use principle component analysis
to reduce feature size and then create csv file for SVM

'''

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import audio_training

def create_model(training_folder):
    '''
    This function takes input of the folder directory that contains
    all raw wav files and mel-spectrogramed raw csv file for building the SVM model
    Then save to a csv file called full.csv
    The full.csv will be needed for analyzing user input
    '''
    classifier = audio_training.save_csv_raw(training_folder)
    x_features = pd.read_csv('trainingData/audio_raw.csv')
    scaler = StandardScaler()
    x_features_scaled = scaler.fit_transform(x_features)
    pca = PCA(n_components=20)
    pca.fit(x_features_scaled)
    x_reduced = pca.transform(x_features_scaled)
    alpha_list = audio_training.add_label()
    full = pd.DataFrame(np.append(classifier[np.newaxis].T, np.vstack((alpha_list, x_reduced)), 1))
    full.to_csv(r'../data/vid/trainingSet/raw/full.csv', index=None, header=False)

'''
This module contains the function that read in user input sound and save as audio_test.csv for fitting the model
'''

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import audio_training

#### user input sound and dimension reduction

def audio_input(wav_input):
    '''
    This function read input of the user input wav file
    Then attach it to the whole data set and run PCA to reduce features
    Save the converted and reduced user input as audio_test.csv for next step SVM
    '''
    user_sound = audio_training.convert_mel_one(wav_input)
    x_features = pd.read_csv('trainingData/audio_raw.csv')
    x_features.loc[len(x_features)] = user_sound
    scaler = StandardScaler()
    x_features_scaled = scaler.fit_transform(x_features)
    pca = PCA(n_components=20)
    pca.fit(x_features_scaled)
    x_reduced = pca.transform(x_features_scaled)
    alpha_list = audio_training.add_label()
    user_output = pd.DataFrame(np.vstack((alpha_list, x_reduced[-1])))
    user_output.insert(0, "00", ['catID', 'userInput'])
    user_output.to_csv(r'userData/audio_test.csv', index=None, header=False)
    
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import audio_training

def create_model(training_folder):
    classifier = audio_training.save_csv_raw(training_folder)
    x_features = pd.read_csv('audio_raw.csv')
    scaler = StandardScaler()
    x_features_scaled = scaler.fit_transform(x_features)
    pca = PCA(n_components=20)
    pca.fit(x_features_scaled)
    x_reduced = pca.transform(x_features_scaled)
    alpha_list = audio_training.add_label()
    full = pd.DataFrame(np.append(classifier[np.newaxis].T, np.vstack((alpha_list, x_reduced)), 1))
    full.to_csv(r'../data/vid/trainingSet/raw/full.csv', index=None, header=False)

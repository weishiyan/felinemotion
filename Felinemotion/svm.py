'''Return the cat emotion
   Imput: tested image and audio data
   Output: cat emotion
   '''

import os
import pandas as pd
from sklearn.svm import LinearSVC

def csv_merge(image, audio):
    '''
        Import test image and audio datasets and merge by catID
        Imput: image and audio datasets in csv
        Output: one dataset with both image and audio data
        '''
# check whether the dataset exist in the current work directory
    if not os.path.exists(image):
        raise ValueError("Invalid input file.")
    if not os.path.exists(audio):
        raise ValueError("Invalid input file.")

    image = pd.read_csv(image)
    audio = pd.read_csv(audio)

    data = audio.merge(image, on='catID')
    data = data.iloc[:, 1:]

    data.to_csv('userData/user_csv.csv')

def classification(term):
    '''
        Return the cat emotion
        Imput: user_csv.csv with both tested image and audio data
        Output: emotion in string
        '''
# emotion should be included in audio file
# import the training dataset
    image = pd.read_csv('trainingData/image.csv')
    audio = pd.read_csv('trainingData/audio.csv')

    data = audio.merge(image, on='catID')

# build the model
    x_value = data.iloc[:, 2:]
    y_value = data.emotion

    clf = LinearSVC(random_state=0, tol=1e-5)
    clf.fit(x_value, y_value)

# read test csv into dataframe
    if not os.path.exists(term):
        raise ValueError("Invalid input file.")

    test = pd.read_csv(term)
    test = test.iolc[:, 1:]

    y_pred = clf.predict(test)
    return(y_pred)

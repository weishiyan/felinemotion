'''
A modules that test audio_input.py

'''

import unittest

import os
import numpy as np
import pandas as pd

import audio_input

class UnitTests(unittest.TestCase):
    def test_wav(self):
        '''
        Check if the input file is wav
        '''
        user_input_file = 'userData/userInput.wav'
        self.assertTrue(user_input_file.endswith('wav'))

    def test_database_raw(self):
        '''
        Check if the raw mel-spectrogramed files from database exist
        '''
        self.assertTrue(os.path. isfile('trainingData/audio_raw.csv'))

    def test_output_shape(self):
        '''
        Check the shape of output file 
        '''
        audio_test = pd.read_csv('userData/audio_test.csv.wav')
        self.assertTrue(audio_test.shape == (1, 21))

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)

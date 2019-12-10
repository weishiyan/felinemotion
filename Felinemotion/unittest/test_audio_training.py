'''
A modules that test audio_training.py

'''

import unittest

import os
import numpy as np
import pandas as pd

import audio_training

class UnitTests(unittest.TestCase):
    def test_length(self):
        '''
        Check if the output 1D array have the right length
        '''
        test = audio_training.convert_mel_one('user_input.wav')
        self.assertTrue(len(test) == 12032)

    def test_classifier_num(self):
        '''
        Check if the returned value match the number of files in data folder
        '''
        test_directory = '../doc/vid/trainingSet/raw'
        classifier = audio_training.save_csv_raw(test_directory)
        self.assertTrue(len(classifier) == len(os.listdir(test_directory)))

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)

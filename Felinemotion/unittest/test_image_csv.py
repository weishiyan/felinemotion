#!/usr/bin/env python
# coding: utf-8

import unittest
import image_output
import os

class UnitTests(unittest.TestCase):
    def test_data(self):
        '''
        Check if the output csv file exist
        '''
        self.assertTrue(os.path. isfile('userData/selected_image.csv'))
    
suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)


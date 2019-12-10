#!/usr/bin/env python
# coding: utf-8

import unittest

import image_analysis
import os
class UnitTests(unittest.TestCase):
    def test_folder(self):
        '''
        Check if the model creates a file for saving cat face images
        '''
        created_folder = 'userData/catFaces/'
        self.assertTrue(os.path.exists(created_folder))

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)


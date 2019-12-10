#!/usr/bin/env python
# coding: utf-8
import os
import unittest
import random_pick_3
class UnitTests(unittest.TestCase):
  def test_image(self):
    '''
    Check if the output file is jpg
    '''
    self.assertTrue(os.path. isfile('userData/user1.jpg'))

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)


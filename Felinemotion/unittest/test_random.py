"""
unit test for module random_pick_3
"""
import os
import unittest
import random_pick_3
class UnitTests(unittest.TestCase):
    """
    unit test
    """
    def test_image(self):
        '''
        Check if the output file is jpg
        '''
        random_pick_3.pick_three('userData/catFaces')
        self.assertTrue(os.path. isfile('userData/user1.jpg'))

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)

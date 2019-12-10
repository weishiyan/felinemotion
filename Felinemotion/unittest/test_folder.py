"""
unit test for image_analysis
"""
import unittest
import os
import image_analysis
class UnitTests(unittest.TestCase):
    """
    unit test
    """
    def test_folder(self):
        """
        Check if the model creates a file for saving cat face images
        """
        image_analysis.cat_detect('userData/frames/', 'haarcascade_frontalcatface.xml')
        created_folder = 'userData/catFaces/'
        self.assertTrue(os.path.exists(created_folder))

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)

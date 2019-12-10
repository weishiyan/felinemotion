"""
Random pick three cat face images for user selection
Imput: cat face images
Output: 3 cat face images
"""
import os
import random
import cv2
def pick_three(path2string):
    """
    import detected cat face images
    random select three images for output
    """
    # dir = "userData/"
    path2 = path2string
    #output = outputstring
    files_out = []
    #  import cat face images
    for root, directories, files in os.walk(path2):
        for file in files:
            files_out.append(os.path.join(root, file))
    # random pick three
    rand = random.sample(files_out, 3)
    dir_name = 'userData/cat3Faces'
    # os.mkdir(dir_name)
    pick1 = rand[1]
    pick2 = rand[2]
    pick3 = rand[0]
    pick1_1 = cv2.imread(pick1)
    pick1_2 = cv2.imread(pick2)
    pick1_3 = cv2.imread(pick3)
    base1 = 'user1.jpg'
    base2 = 'user2.jpg'
    base3 = 'user3.jpg'
    cv2.imwrite(os.path.join('userData/', base1), pick1_1)
    cv2.imwrite(os.path.join('userData/', base2), pick1_2)
    cv2.imwrite(os.path.join('userData/', base3), pick1_3)

"""
Output selected image to csv
Imput: one cat face image
Output: csv file
"""
import cv2
import numpy as np
import pandas as pd
# load selected image

def image_output(directory, image):
    """
    Import selected image and output to datasets
    """
    # dir = "userData/"
    # imge = "user1.jpg"
    image_loc = directory + image
    csv_loc = directory + 'selected_image.csv'
    img = cv2.imread(image_loc, 0)
    img2 = np.asarray(img).reshape(-1)
    num = 400
    img_data = []
    num_data = []
    for i in range(0, num):
        j = i * 100 + 1
        sum_img = sum(img2[j:100 + j])
        avg_img = sum_img / 100
        i_list = i + 1
        num_data.append(i_list)
        img_data.append(avg_img)
    df_img = pd.DataFrame({'catID':num_data, 'userInput':img_data})
    df_img = df_img.transpose()
    df_img.to_csv(csv_loc, header=False)

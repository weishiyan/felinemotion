import os


def clear_folder():
    img_dir_1 = 'userData/catFaces'
    img_dir_2 = 'userData/cat3Faces'
    # img_dir_3 = 'userData/frames'
    filelist1 = os.listdir(img_dir_1)
    filelist2 = os.listdir(img_dir_2)
    # filelist3 = os.listdir(img_dir_3)
    for file1 in filelist1:
        os.remove(os.path.join(img_dir_1,file1))
    for file2 in filelist2:
        os.remove(os.path.join(img_dir_2, file2))
    # for file3 in filelist3:
    #     os.remove(os.path.join(img_dir_3,file3))
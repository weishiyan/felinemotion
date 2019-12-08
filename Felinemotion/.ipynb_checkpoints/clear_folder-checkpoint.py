import os


def clear_folder():
    img_dir_1 = 'userData/catFaces'
    img_dir_2 = 'userData/cat3Faces'
    filelist1 = os.listdir(img_dir_1)
    filelist2 = os.listdir(img_dir_2)
    for file1 in filelist1:
        os.remove(os.path.join(img_dir_1,file1))
    for file2 in filelist2:
        os.remove(os.path.join(img_dir_2,file2))
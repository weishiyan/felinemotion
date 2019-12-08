import os
import random
import cv2
def pick_three(path2String, outputString):
	"""
	test
	"""
	path2 = path2String
	#Images with cat face file save path
	#path2 = 'e:\\2019fall\\CSE583\\FellinEmotion\\cat-face-detector\\image_select\\'
	output = outputString
	#Images with cat face file save path
	#output = 'e:\\2019fall\\CSE583\\FellinEmotion\\cat-face-detector\\image_output\\'
	files_out = []
	# r=root, d=directories, f = files
	for root, directories, files in os.walk(path2):
		for file in files:
			files_out.append(os.path.join(root, file))
	rand = random.sample(files_out, 3)
	pick1 = rand[1]
	pick2 = rand[2]
	pick3 = rand[0]
	pick1_1 = cv2.imread(pick1)
	pick1_2 = cv2.imread(pick2)
	pick1_3 = cv2.imread(pick3)
	base1 = os.path.basename(pick1)
	base2 = os.path.basename(pick2)
	base3 = os.path.basename(pick3)
	cv2.imwrite(os.path.join(output, base1), pick1_1)
	cv2.imwrite(os.path.join(output, base2), pick1_2)
	cv2.imwrite(os.path.join(output, base3), pick1_3)

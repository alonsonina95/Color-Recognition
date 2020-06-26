import numpy as np
from cv2 import cv2

# anyColor = np.uint8([[[165,42,42]]]) #HERE GOES THE COLOR IN BGR
# hsvAnyColor = cv2.cvtColor(anyColor, cv2.COLOR_BGR2HSV)
# lowerLimit = hsvAnyColor[0][0][0] - 10,100,100
# upperLimit = hsvAnyColor[0][0][0] + 10,255,255
# print (hsvAnyColor)
# print (lowerLimit)
# print (upperLimit)

def RGB2HEX(color):
#returns a string that simply displays the hex value for the respective color
	return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_image(image_path):
	image = cv2.imread(image_path)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	return image

class Red:
	upperRange = np.array([180,255,255], np.uint8)
	lowerRange = np.array([136,87,111], np.uint8)
class Green:
	upperRange = np.array([70,255,255])
	lowerRange = np.array([50,100,100])
class Yellow:
	upperRange = np.array([60,255,255], np.uint8)
	lowerRange = np.array([22,60,200], np.uint8)
class Blue:
	upperRange = np.array([110,255,255], np.uint8)
	lowerRange = np.array([99,115,150], np.uint8)
class Aqua:
	upperRange = np.array([100,255,255])
	lowerRange = np.array([80,100,100])
class Magenta:
	upperRange = np.array([160,255,255])
	lowerRange = np.array([140,100,100])
class Black:
	upperRange = np.array([-10,100,100])
	lowerRange = np.array([10,255,255])
class Brown:
	upperRange = np.array([110,100,100])
	lowerRange = np.array([130,255,255])

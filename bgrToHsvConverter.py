import numpy as np
import cv2

#anyColor = np.uint8([[[0,255,255]]]) #HERE GOES THE COLOR IN BGR
#hsvAnyColor = cv2.cvtColor(anyColor, cv2.COLOR_BGR2HSV)
#lowerLimit = hsvAnyColor[0][0][0] - 10,100,100
#upperLimit = hsvAnyColor[0][0][0] + 10,255,255
#print (hsvAnyColor)
#print (lowerLimit)
#print (upperLimit)

class Green:
	upperRange = np.array([70,255,255])
	lowerRange = np.array([50,100,100])
class Yellow:
	upperRange = np.array([40,255,255])
	lowerRange = np.array([20,100,100])
class Blue:
	upperRange = np.array([130,255,255])
	lowerRange = np.array([110,100,100])
class Aqua:
	upperRange = np.array([100,255,255])
	lowerRange = np.array([80,100,100])
class Magenta:
	upperRange = np.array([160,255,255])
	lowerRange = np.array([140,100,100])

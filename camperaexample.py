import cv2
import picamera
import numpy as np
import matplotlib.pyplot as plt

class Yellow:
	lower = np.array([255,255,240])
	upper = np.array([181,166,66])

class YellowToGreen:
	lower: np.array([223,255,0])
	upper: np.array([75,83,32])
class Green: 
	lower = np.array([178,236,93])
	upper = np.array([65,72,51])
class GreenToBlue
	lower = np.array([127,255,212])
	upper = np.array([26,36,33])
class CyanColorBlue:
	lower = np.array([231,254,255])
	upper= np.array([47,79,79])
class CyanBlue:
	lower = np.array([240,248,255])
	upper = np.array([0,33,71])
class Blue:
	lower = np.array([248,248,255])
	upper = np.array([0,32,102])
class BlueMagenta:
	lower = np.array([191,148,288])
	upper = np.array([105,53,156])
class Magenta: 
	lower = np.array([209,159,232])
	upper = np.array([93,57,84])
class MagentaPink:
	lower = np.array([255,240,245])
	upper = np.array([97,64,81])
class Pink:
	lower = np.array([255,209,220])
	upper = np.array([86,3,25])
class PinkRed:
	lower = np.array([255,193,204])
	upper = np.array([101,0,11])
class Red:
	lower = np.array([255,250,250])
	upper = np.array([50,20,20])
class RedOrange:
	lower = np.array([255,253,102])
	upper = np.array([109,53,26])
class OrangeYellow: 
	lower = np.array([255,248,220])
	upper = np.array([150,113,23])
class Gray:
	lower = np.array([220,220,220])
	upper = np.array([52,52,52])
class White:
	lower = np.array([255,255,255])
	upper = np.array([255,255,255])
class Black:
	lower = np.array([0,0,0])
	u[[er = np.array([0,0,0])
yellowRanges = Yellow()
greenRanges = Green()
image = cv2.imread('example1.jpg')
width = 800
height = 500 
dimensions=(width, height)
resize_image = cv2.resize(image, dimensions)
hsv = cv2.cvtColor(resize_image, cv2.COLOR_BGR2HSV)
lower_range = greenRanges.lower
upper_range = greenRanges.upper
mask = cv2.inRange(hsv, lower_range, upper_range)
while True:
	cv2.imshow('Image', resize_image)
	cv2.imshow('Mask', mask)
	if cv2.waitKey(1) & 0xFF == 27:
		break
cv2.destroyAllWindows()

import cv2
import picamera
import numpy as np
import matplotlib.pyplot as plt

class Yellow:
	lower = np.array([15,25,25])
	upper = np.array([36,255,255])
class Green: 
	lower = np.array([36,25,25])
	upper = np.array([70,255,255])
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

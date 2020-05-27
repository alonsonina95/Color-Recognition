import cv2
import picamera
import numpy as np
import matplotlib.pyplot as plt
from bgrToHsvConverter import Blue, Green, Yellow, Aqua, Magenta
colorToBeDetected = Yellow()
image = cv2.imread('example1.jpg')
width = 800
height = 500 
dimensions=(width, height)
resize_image = cv2.resize(image, dimensions)
rgb = cv2.cvtColor(resize_image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(rgb, colorToBeDetected.lowerRange, colorToBeDetected.upperRange)
while True:
	cv2.imshow('Image', resize_image)
	cv2.imshow('Mask', mask)
	if cv2.waitKey(1) & 0xFF == 27:
		break
cv2.destroyAllWindows()

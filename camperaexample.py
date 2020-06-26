from cv2 import cv2
from picamera import PiCamera
import numpy as np
import matplotlib.pyplot as plt
from rgbToHex import get_image, Red, Blue, Green, Yellow, Aqua, Magenta, Black, Brown
from time import sleep

# camera = PiCamera()
# camera.rotation = 180
# camera.start_preview()
# sleep(5)
# camera.capture('/home/pi/image.jpg')
# camera.stop_preview()
# redObject = Red()
# blueObject = Blue()
# yellowObject = Yellow()
# image = cv2.imread('image.jpg')
# width = 800
# height = 500 
# dimensions=(width, height)
# resize_image = cv2.resize(image, dimensions)
# imageConvertedToRgb = get_image(resize_image)
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# red = cv2.inRange(hsv, redObject.lowerRange, redObject.upperRange)
# blue = cv2.inRange(hsv, blueObject.lowerRange, blueObject.upperRange)
# yellow = cv2.inRange(hsv, yellowObject.lowerRange, yellowObject.upperRange)
# rgb = cv2.cvtColor(resize_image, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(rgb, colorToBeDetected.lowerRange, colorToBeDetected.upperRange)

# while True:
# 	cv2.imshow('Image', resize_image)
# 	cv2.imshow('Mask', mask)
# 	if cv2.waitKey(1) & 0xFF == 27:
# 		break
# cv2.destroyAllWindows()

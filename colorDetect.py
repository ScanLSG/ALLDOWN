# 使用OpenCV和Python检测特定颜色
# https://www.codenong.com/detection-of-a-specific-color-blue-here-using-opencv-with-python/

# black (0, 0, 0)   white(255, 255, 255)

import cv2
import numpy as np
from numpy.core.defchararray import upper

# loading image
img_BGR = cv2.imread('D:\\Code\\ALLDOWN\\ALLDOWN\\alcoholImage\\2.jpg')
img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)

# definition blue
blue_lower_range = np.array([110, 50, 50])
blue_upper_range = np.array([130, 255, 255])

mask = cv2.inRange(img_HSV, blue_lower_range, blue_upper_range)
cv2.imshow('mask', mask)
#cv2.imshow('image', img_BGR)

a = cv2.findNonZero(mask)
print(a)
print(type(a))

cv2.waitKey(0)
















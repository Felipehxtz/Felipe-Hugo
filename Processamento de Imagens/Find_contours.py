import numpy as np
import cv2

img = cv2.imread('img02.png') # Read image
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert Color to gray scale
ret, thresh = cv2.threshold(imgray, 70, 256, 1) # Threshold value is applied
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #Find contours of the gray scale image
print("Number of contours = " + str(len(contours))) # Show number of contour in the image
print(contours[0])

cv2.drawContours(img, contours, -1, (0, 0, 255), 3) #Draw contour in the original image


cv2.imshow('Image', img)# Show result

cv2.waitKey(0)# Finish
cv2.destroyAllWindows()
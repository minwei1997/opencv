import cv2 as cv 
import numpy as np

img = cv.imread('lena.jpg')
cv.imshow('lena',img)

cv.waitKey(0)
cv.destroyAllWindows()

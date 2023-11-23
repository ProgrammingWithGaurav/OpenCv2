import cv2
print('Imported')

img = cv2.imread('Assets/')

cv2.imshow('Output', img)
cv2.waitKey(0)
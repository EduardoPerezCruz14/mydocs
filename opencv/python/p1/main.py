import cv2

image = cv2.imread('/home/edu/Pictures/image.png')

cv2.imshow('image',image)

cv2.waitKey(0) # wait until press a "esc" keyboard key
cv2.destroyAllWindows()
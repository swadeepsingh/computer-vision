# import package
import cv2

# init web cam
cam = cv2.VideoCapture(0)

# read frame from web cam
ret, image = cam.read()

# convert image to gray scale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show image in seperate window
cv2.imshow("output", image)

# wait for key press
cv2.waitKey(0)

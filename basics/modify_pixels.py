# Read an image file and executes some basic operations on pixel level

# import package
import cv2

# read image from HD
image = cv2.imread("aero1.jpg")

# read color values at position y, x
y = 100
x = 50
(b, g, r) = image[y, x]

# print color values to screen
print(b,g,r)

# set pixel color to RED in BGR color scheme
image[y, x] = (0, 0, 255)

# choose region of interest at (x, y) with dimension 50x50 pixel
region_of_interest = image[y:y+50, x:x+50]

# show image on screen
cv2.imshow("Bild", image)

# show region of interest in seperate window
cv2.imshow("ROI", region_of_interest)

# set all ROI pixels to green
region_of_interest[:, :] = (0, 255, 0)

# now show modified image, not that ROI is a "pointer" to the original image
cv2.imshow("Modified Image", image)

# wait for a key - important, otherwise nothing would be visible
cv2.waitKey(0)

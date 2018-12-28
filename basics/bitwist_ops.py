import numpy as np
import cv2

# Bitwise operations AND,NOT, OR, XOR

sz = 256
img1 = np.zeros((sz,sz,3), np.uint8)
img1[:,0:sz//2] = (0,0,255)
img1[:,sz//2:sz] = (0,255,0)
img2 = np.ones((sz,sz,3), np.uint8)
img2[0:sz//2,:] = (0,255,255)
img2[sz//2:sz,:] = (255,120,0)

bit_and = cv2.bitwise_and(img2, img1)
bit_or = cv2.bitwise_or(img2, img1)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
cv2.imshow("bit_not", bit_not)
cv2.imshow("bit_not2", bit_not2)

cv2.waitKey(0)
cv2.destroyAllWindows()

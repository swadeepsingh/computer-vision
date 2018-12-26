# import packages
import cv2


# load sample image
def load_image():
    img = cv2.imread("lena.jpg")
    return img


# LAB colorspace
def covtLAB(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    return lab


# YCrCb colorspace
def covtYCrCb(img):
    ycrbc = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    return ycrcb


# HSV colorspace
def covtHSV(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return hsv
    

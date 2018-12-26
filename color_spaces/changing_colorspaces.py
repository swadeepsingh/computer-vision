# import packages
import cv2


# load sample image
def load_image():
    img = cv2.imread("lena.jpg")
    return img


# Gray colorspace
def covtGray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray
    
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
    

img = load_image()
gray_image = covtGray(img)
lab_img = covtLAB(img)
ycrbc_img = covtYCrCb(img)
hsv_img = covtHSV(img)
cv2.imshow('original image',img)
cv2.imshow('gray image', gray_image)
cv2.imshow('Lab image',lab_img)
cv2.imshow('YCrCb image',ycrbc_img)
cv2.imshow('HSV image',hsv_img)
cv2.waitKey(0)

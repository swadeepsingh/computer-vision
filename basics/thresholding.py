# import package
import cv2


def covt_gray(img):
    """
     convert image to grayscale

     @param img: color image
     @return gray scale converted image
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


def apply_binary_thresh(img, color_id=0):
    """
    appliy binary thresholding

    @param img: input color image
    @param color_id: 0 for color image thresholding and 1 for graycale image thresholding
    @return: transformed image
    """
       
    if color_id == 0:
        retval, threshold = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
        return threshold
    elif color_id==1:
        grayscaled = covt_gray(img)
        retval, threshold = cv2.threshold(grayscaled, 50, 255, cv2.THRESH_BINARY)
        return threshold


def apply_adaptiv_gaussian_thresh(grayscaled):
    """
     apply adaptive thresholding, which will attempt to vary the threshold

     @param grayscaled: grayscale image
     @return: transformed image
    """
    thres = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    return thres

    
def apply_otsu_thresh(grayscaled):
    """
     apply Otsu's threshold

     @param grayscaled: grayscale image
     @return: transformed image
    """
    retval2, threshold2 = cv2.threshold(grayscaled, 30, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return threshold2


img = cv2.imread('../data/sudoku-original.jpg')
grayscaled = covt_gray(img)
color_tx_img = apply_binary_thresh(img, color_id=0)
gray_tx_img = apply_binary_thresh(img, color_id=1)
adaptive_tx_img = apply_adaptiv_gaussian_thresh(grayscaled)
otsu_tx_img = apply_otsu_thresh(grayscaled)

cv2.imshow('original', img)
cv2.imshow('binary threshold (on color image)', color_tx_img)
cv2.imshow('binary threshold (on grayscale image)', gray_tx_img)
cv2.imshow('Adaptive threshold', adaptive_tx_img)
cv2.imshow('Otsu threshold', otsu_tx_img)
cv2.waitKey(0)

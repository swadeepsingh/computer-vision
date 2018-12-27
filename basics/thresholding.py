# import package
import cv2

def covtGray(img):
    '''
     convert image to grayscale
     
     @param img: color image
     @return gray scale converted image
    '''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


def apply_binary_thresh(img, color_id=0):
    '''
    appliy binary thresholding 
    
    @param img: input color image
    @param color_id: 0 for color image thresholding and 1 for graycale image thresholding
    '''
       
    if (color_id == 0):
        retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
        cv2.imshow('original',img)
        cv2.imshow('binary threshold',threshold)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elsif (color_id==1):
        grayscaled = covtGray(img)
        retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
        cv2.imshow('original',img)
        cv2.imshow('binary threshold (on grayscale image)',threshold)
        cv2.waitKey(0)
        cv2.destroyAllWindows()    
        

def apply_adaptiv_gaussian_thresh(grayscaled):
    '''
     apply adaptive thresholding, which will attempt to vary the threshold
     
     @param grayscaled: grayscale image
    '''
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imshow('original',img)
    cv2.imshow('Adaptive threshold',th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def apply_otsu_thresh(grayscaled):
    '''
     apply Otsu's threshold 
     
     @param grayscaled: grayscale image
    '''
    retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('original',img)
    cv2.imshow('Otsu threshold',threshold2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   

img = cv2.imread('sudoku-original.jpg')
apply_binary_thresh(img, color_id=0)
apply_binary_thresh(img, color_id=1)
grayscaled = covtGray(img)
apply_adaptiv_gaussian_thresh(grayscaled)
apply_otsu_thresh(grayscaled)

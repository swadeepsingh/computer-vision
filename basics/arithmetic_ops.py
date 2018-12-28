import cv2 as cv
import numpy as np


def addition_example():
    """
    Image addition example
    """

    # dimension for sample image
    width = 512
    height = 512

    # create empty images with green and red channel
    green = np.zeros((height, width, 3), np.uint8)
    green[:, :] = (0, 255, 0)
    red = np.zeros((height, width, 3), np.uint8)
    red[:, :] = (0, 0, 255)

    # add operation
    add_op = red + green

    # display results
    canvas = np.hstack((red,green,add_op))
    cv.imshow("output:(red + green = yellow)", canvas)
    cv.waitKey(0)


def image_blending():
    """
    Image blending example
    """    
    img1 = cv.imread('../data/udacity.jpg')
    img2 = cv.imread('../data/opencv.png')
    dst = cv.addWeighted(img1, 0.6, img2, 0.4, 0)
    np_hstack = np.hstack((img1,img2,dst))
    cv.imshow('output:(img1, img2, output)', np_hstack)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    addition_example()
    image_blending()

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:02:10 2021

@author: Kaan Baykara
"""

import cv2 as cv


def main():
    
    """ This code applies canny edge detection and threshold on image """
    
    image_city = cv.imread('sample_inputs/city.jpg')

    image_gray = cv.cvtColor(image_city, cv.COLOR_BGR2GRAY)

    blurred_city = cv.GaussianBlur(image_gray, (5, 5), 15)

    variable, threshold = cv.threshold(blurred_city, 127, 255, cv.THRESH_BINARY)

    canny_edge_detection = cv.Canny(blurred_city, 100, 200)

    cv.imshow('canny', canny_edge_detection)

    cv.imshow('threshold', threshold)

    cv.waitKey(0)

    cv.destroyAllWindows()

if __name__ == "__main__":
    main()






# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:13:52 2021


@author: Kaan Baykara
"""

import cv2 as cv

def rotation(image, angle, rotation_point = None):
    """
    This function will rotate your image according to the angle and reference point (rotation_point)
    If the rotation point (rotation_point) is not specified, the value is assigned according to the width and height.
    """
    height, width = image.shape[:2]
    
    if rotation_point == None:
        rotpoint = (height//2, width//2)
    
    rotation_matrix = cv.getRotationMatrix2D(rotpoint, angle, 1)
    
    dimension = (height, width)
    
    return cv.warpAffine(image, rotation_matrix, dimension)

def main():    
    image = cv.imread("sample_inputs/city.jpg")
    
    # Resized the image 600x600 pixel. 
   
    resized = cv.resize(image, (600, 600), interpolation = cv.INTER_CUBIC)

    rotated = rotation(resized, 25)
    
    cv.imshow("original_image", image)   
    cv.imshow("rotated_image", rotated)
    cv.imshow("resized_image", resized)

    cv.waitKey(0)

    cv.destroyAllWindows()
    
if __name__ == "__main__":
    main()
















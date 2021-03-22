# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:02:08 2021

@author: Kaan Baykara
"""

import cv2 as cv
    
def resize_image(image, height, width):
    
    # This function resizes input image using the height and width variables. 
    
    return cv.resize(image, (height, width), interpolation = cv.INTER_CUBIC)

def color_transform(image):

    # This function transform BGR images to Gray image    

    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def threshold(image, threshold_value):
    
    # This function converts input image into a binary image based on the threshold value.    

    return cv.threshold(image, threshold_value, 255, cv.THRESH_BINARY)

def blur_option(image, blur_type, matrix_size):
    
    """ 
    This function can apply gaussian or avarage or median filter  
    blur_type should be string 
    matrix_size should be square matrix so write a single variable.
    """
    
    if  blur_type == "gaussian":
        
        return cv.GaussianBlur(image, (matrix_size, matrix_size), 2)
    
    elif blur_type == "avarage":
        
        return cv.blur(image, (matrix_size, matrix_size))
    
    elif blur_type == "median":
        
        return cv.medianBlur(image, matrix_size)

def main():    
    image=cv.imread("sample_inputs/input_sample.jpeg")    
    
    resized_image = resize_image(image, 750, 750)
    color_transform_result = color_transform(resized_image) 
    retval, thresh = threshold(color_transform_result, 125)
    blur_option_result = blur_option(color_transform_result, "median", 7)

    cv.imshow("resized_image", resized_image)
    cv.imshow("recolored_image", color_transform_result)
    cv.imshow("blurred_image", blur_option_result)
    cv.imshow("threshold_image", thresh)

    cv.waitKey(0)
    cv.destroyAllWindows()
    
if __name__ == "__main__":
    main()














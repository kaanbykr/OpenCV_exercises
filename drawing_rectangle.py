# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:32:58 2021

@author: Kaan Baykara
"""

import cv2 as cv
from matplotlib import pyplot as plt


def rescale_image(image, scale=0.50):        
    """
    With this function, you can resize your picture by specifying the scale factor.
    If you do not enter a scale variable, the function will accept the scale variable as 0.5
    """
    
    wi = int(image.shape[1]*scale)
    hei = int(image.shape[0]*scale)
    dimension = (wi, hei)
    return cv.resize(image, dimension, interpolation = cv.INTER_AREA)


def main():
    
    image = cv.imread("sample_inputs/dog.jpg")    

    resized_image = rescale_image(image)
    
    # This function allows to see the image on the plot 
    
    plt.figure(0)
    plt.imshow(resized_image)
    
    """  
        cv.rectangle function allow to draw rectangle on image 
        cv.putText function allow to write rectangle on image 
    """
    
    cv.rectangle(resized_image, (450 , 100), (700, 400), (0, 255, 0), thickness=2)  
    
    cv.putText(resized_image, "Dog", (550, 450), cv.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 2)

    cv.imshow("drawing_line_and_rectangle", resized_image)

    cv.waitKey(0)
    cv.destroyAllWindows()
    
if __name__ == "__main__":
    main()











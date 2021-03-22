# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:07:46 2021

@author: Kaan Baykara
"""


import cv2 as cv

def main():
    """ This code allows us to combine the 2 pictures with the bitwise method in various ways."""
   
    dog_image = cv.imread("sample_inputs/dog.jpg")
    city_image = cv.imread("sample_inputs/city.jpg")
    
    cropped_dog = dog_image[0:600, 1100:1500]
    cropped_city = city_image[0:600, 200:600]

    gray_city = cv.cvtColor(cropped_city, cv.COLOR_BGR2GRAY)
    gray_dog = cv.cvtColor(cropped_dog, cv.COLOR_BGR2GRAY)

    # Blurring the images with Gaussian blur
    
    blur_city = cv.GaussianBlur(gray_city, (5, 5), 2, sigmaY=2)
    blur_dog = cv.GaussianBlur(gray_dog, (5, 5), 2, sigmaY=2)


    # Bitwise and - or  operations
    
    bitwise_and = cv.bitwise_and(blur_city, blur_dog)
    bitwise_or = cv.bitwise_or(blur_city, blur_dog)


    cv.imshow("bitwise and", bitwise_and)
    cv.imshow("bitwise or", bitwise_or)


    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()




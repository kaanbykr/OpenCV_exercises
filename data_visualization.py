# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:52:41 2021

@author: Kaan Baykara
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def main():
    
    dog_image = cv.imread("sample_inputs/dog.jpg")

    city_image = cv.imread("sample_inputs/city.jpg")

    rgb_dog = cv.cvtColor(dog_image, cv.COLOR_BGR2RGB)

    rgb_city = cv.cvtColor(city_image, cv.COLOR_BGR2RGB)

    plt.figure(0)
    plt.imshow(rgb_dog)
    
    # Cropping is done to make the pictures the same size. 
    
    cropped_dog = rgb_dog[250:550, 900:1350]
    cropped_city = rgb_city[450:750, 100:550]


    # Adding two diffrent image to each other.
    
    combine_samples = cv.add(cropped_dog, cropped_city)

    cv.imshow("dog_city", combine_samples)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Creation of Filters
   
    filter_small = np.ones((3,3), np.float32)/9

    filter_medium = np.ones((15,15), np.float32)/225

    filter_large = np.ones((100,100), np.float32)/10000


    # Filtering the images
    
    filtered_small_matrix = cv.filter2D(cropped_city, -1, filter_small)

    filtered_medium_matrix = cv.filter2D(cropped_city, -1, filter_medium)

    filtered_large_matrix = cv.filter2D(cropped_city, -1, filter_large)

    # Visualization the images using matplotlib library

    plt.subplot(331), plt.imshow(filtered_small_matrix, cmap=plt.get_cmap('gray')), plt.title('3x3 kernel')
    plt.xticks([]), plt.yticks([])

    plt.subplot(332), plt.imshow(filtered_medium_matrix, cmap=plt.get_cmap('gray')), plt.title('9x9  kernel')
    plt.xticks([]), plt.yticks([])

    plt.subplot(333), plt.imshow(filtered_large_matrix, cmap=plt.get_cmap('gray')), plt.title('100x100 kernel')
    plt.xticks([]), plt.yticks([])

    plt.show()
    
if __name__ == "__main__":
    main()











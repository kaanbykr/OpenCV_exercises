# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:53:43 2021

@author: Kaan Baykara
"""

import cv2 as cv

def main():
   
    """With this code, the location of the template in the original image can be detected."""
    
    image = cv.imread("sample_inputs/input_sample.jpeg")
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    template = cv.imread("sample_inputs/input_template.jpeg")
    template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    result = cv.matchTemplate(gray_image, template, cv.TM_CCOEFF_NORMED)

    cv.imshow("template", template)
    cv.imshow("original_image", image)
    cv.imshow("result", result)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()




















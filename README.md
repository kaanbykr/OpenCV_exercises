# OpenCV_exercises

## Goal
    
The purpose of writing these codes is to learn and practice the Python OpenCV library.
To make this code easy to read and understand, it has been tried to be written by the python coding style guidelines and clean code techniques.

## Development
While preparing this repository, OpenCV documentation and [freeCodeCamp.org Youtube channel](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) were used.

## Requirements
- Python 3.6
- OpenCV 2

## How to Use 
Once you clone the repository, you can run samples with Python 3.6+

Create a virtual environment;
`python3 -m venv .env`

Run the following command to install all requirements;
`pip install -r requirements.txt`

The input images and codes used for the code to work properly must be in **the same folder**.

If you want to import your input images, you can also use your input images. 

Make sure that the new images must be the same as the names in code files.

## Code Files

### `bitwise_operations.py`
This code allows us to combine the 2 pictures with the bitwise method
### `canny_threshold.py`
This code applies canny edge detection and threshold on image
### `data_visualization.py`
This code applies blur operations and visualization of the images using matplotlib library
### `drawing_rectangle.py`
This code allows drawing a rectangle on the image
### `filtering_blurring.py`
This code resizes and blurring your image
### `rotation.py`
This code rotate your image according to the angle and reference point
### `template_matching.py`
With this code, the location of the template in the original image can be detected.


## Road Map 
In fact, I wanted to pass input file paths as arguments to scripts, but I haven't finished yet.

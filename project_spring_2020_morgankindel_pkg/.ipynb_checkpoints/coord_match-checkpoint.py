%%writefile coordinate_match.py 


#import required packages 
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from PIL import Image
#-------------------------------------------------------
def process_input_img():
    """Takes unprocessed confocal images centered on third ventricle of mouse brain, rescales and sets threshold. """
    
    #load input image from Sample images file folder or set new path for new input image 
    input_img = cv2.imread('./Sample_images/img7.jpg')
    
    #scale input image and set threshold
    scale_percent = 8 #percent of original image size
    width = int(input_img.shape[1]* scale_percent/100)
    height = int(input_img.shape[0]* scale_percent/100)
    dim = (width, height)
    input_img_resized = cv2.resize(input_img, dim, interpolation = cv2.INTER_AREA)
    thresh, input_img_bw = cv2.threshold(input_img_resized,50,250,cv2.THRESH_BINARY)
    return process_input_image
#-------------------------------------------------------
def template_grid():
    
    """Creates 3x3 grid of all reference images that the input image will be compared against the processed input image"""
    
    import math

    #load reference image file and set output file name
    template_img_dir = './Reference_images'
    result_grid_filename = './grid.jpg'
    result_figsize_resolution = 40 # 1 = 100px

    #create list variable that lists files in reference images, and length variable for counting iterations 
    images_list = sorted(os.listdir(template_img_dir))
    images_count = len(images_list)
    print('Images: ', images_list)
    print('Images count: ', images_count)

    # Calculate the grid size:
    grid_size = math.ceil(math.sqrt(images_count))

    # Create plt plot:
    fig, axes = plt.subplots(grid_size, grid_size, figsize=(result_figsize_resolution, result_figsize_resolution))


    current_file_number = 0

    # create an image grid of reference images that will be compared to the input image. 
    for image_filename in images_list:
        x_position = current_file_number % grid_size
        y_position = current_file_number // grid_size
        plt_image = plt.imread(template_img_dir + '/' + images_list[current_file_number])
        axes[x_position, y_position].imshow(plt_image)

        axes[0,0].set_title('Bregma: -0.46', fontsize=50)
        axes[0,1].set_title('Bregma: -0.58', fontsize=50)
        axes[0,2].set_title('Bregma: -0.70', fontsize=50)
        axes[1,0].set_title('Bregma: -0.82', fontsize=50)
        axes[1,1].set_title('Bregma: -0.94', fontsize=50)
        axes[1,2].set_title('Bregma: -1.00', fontsize=50)
        axes[2,0].set_title('Bregma: -1.06', fontsize=50)
        axes[2,1].set_title('Bregma: -1.12', fontsize=50)
        axes[2,2].set_title('Bregma: -1.32', fontsize=50)

        print((current_file_number + 1), '/', images_count, ': ', image_filename)

        current_file_number += 1

    plt.subplots_adjust(left=0.0, right=.9, bottom=0.0, top=.9)
    plt.savefig(result_grid_filename)
    return(result_grid_filename)

#-------------------------------------------------------
def 


    
    



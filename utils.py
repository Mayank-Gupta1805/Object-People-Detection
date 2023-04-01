import cv2

import matplotlib.pyplot as plt
import numpy as np

# Function start here
def plotting(image_src, title):
    '''
    Plot image
    '''
    plt.figure( figsize= (5,5))
    plt.title(title)
    if title in ["Gamma Correction", "Thresholding", "Dilation + Erosion"]:
        plt.imshow(image_src, cmap="gray", vmin=0, vmax=255)
    else:
        plt.imshow(image_src, 'gray')
    plt.show()


def crop(image, start_y, end_y, start_x, end_x):
    '''
    Crop Image
    '''
    img_cropped = image[start_y:end_y, start_x:end_x]
    return img_cropped


def padding(image, pad_height, pad_width):
    '''
    Apply padding to Image
    '''
    H, W, C = image.shape
    out = np.zeros((H + (2 * pad_height), W + (2 * pad_width), C))
    for c in range(C):
        out[pad_height:H + pad_height, pad_width:W + pad_width, c] = image[:, :, c]
    return out


def resize(image, x, y):
    '''
    Resize Image
    '''
    img_resized = cv2.resize(image, (x, y))
    return img_resized

def get_segments(image):
    '''
    Segment Image into 4 quadrants for better analysis
    '''
    width = image.shape[1]
    height = image.shape[0]

    xsize = (width // 2)
    ysize = (height // 2)

    seg_1 = crop(image, 0, ysize, 0, xsize)
    seg_2 = crop(image, 0, ysize, xsize, width)
    seg_3 = crop(image, ysize, height, 0, xsize)
    seg_4 = crop(image, ysize, height, xsize, width)

    return [seg_1, seg_2, seg_3, seg_4]
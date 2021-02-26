import cvlib
import cv2
import random

"""
Emil Wiman, emiwi425
August Nordin, augno992
Laboration 5, del B. Funktionell programmering och högre ordningens funktioner.
"""


def pixel_constraint(hlow,hhigh,slow,shigh,vlow,vhigh):
    """
    Function that returns a function that returns a 1 if its in the correct
    range and 0 i its out of bounds.
    """
    def compareer(pixel):
        """
        Given a pixel value in the form of a tuple return a 1 if the pixel value
        is in range of the value predetermined in pixel_constraint and a 0
        if the value is out of the predetermined bounds.
        """
        (h,s,v) = pixel
        if h > hlow and h < hhigh and \
                s > slow and s < shigh and \
                v > vlow and v < vhigh:
            return 1
        else:
            return 0
    return compareer


def cvimg_to_list(image):
    """
    This function takes an OpenCV-picture and returns a list
    with BGR-tuplers.
    """
    picsize = (image.shape[0], image.shape[1])
    colrange = []
    for px in range(picsize[0]):
        for py in range(picsize[1]):
            temp = (image[px, py][0], image[px,py][1], image[px,py][2])
            colrange.append(temp)
    return colrange

def generator_from_image(orig_list):
    """
    This function returns a function that returns the index of the input index.
    """
    def generated_list(index):
        """
        From a list given in generator_from_image given an idex returns the
        value of that index.
        """
        pixel = orig_list[index]
        return pixel
    return generated_list


def generator1(index):
    """
    Generates a  night sky.
    """
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)


def combine_images(hsv_list, cond, gen1, gen2):
    """
    Function that combines images
    """
    cond_list = []
    rbg_list = []
    for i in range(len(hsv_list)):
        hold = cond(hsv_list[i])
        cond_list.append(hold)
    for i in range(len(hsv_list)):
        rbg_list.append(gen2(i))
    for i in range(len(hsv_list)):
        if cond_list[i] == 1:
            rbg_list[i] = gen1(rbg_list[i])
    return rbg_list


def gradient_condition(col_tup):
    """
    Generates a value from a grayscale image based on how black or white the
    picture is.
    """
    ref_val = col_tup [1]
    result = ref_val/255
    return  round(result,1)

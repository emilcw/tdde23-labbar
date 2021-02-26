import cvlib
import cv2
import random
<<<<<<< HEAD
from lab5a import *

def create_lock(code,message):
    def lock(code2):
        if code == code2:
            print(message)
        else:
            print("Fel kod!")
    return lock
=======
>>>>>>> 115316dcff4362f71f7d83a83dc735e33e9750ed


def pixel_constraint(hlow,hhigh,slow,shigh,vlow,vhigh):
    def compareer(pixel):
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
<<<<<<< HEAD
    def generatedpixel(index):
        pixel = orig_list[index]
        return pixel
    return generatedpixel
=======
    """
    This function returns a function that returns the index of the input index.
    """
    def generated_list(index):
        pixel = orig_list[index]
        return pixel
    return generated_list
>>>>>>> 115316dcff4362f71f7d83a83dc735e33e9750ed


def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
<<<<<<< HEAD
    return (val,val,val)


def combine_images(hsv_list,condition,gen1,gen2):
    return None


def condition():
    """
    Returns a value between 0 and 1.
    """


def gradient_condition(b,g,r):
=======
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
    ref_val = col_tup [1]
    result = ref_val/255
    return  round(result,1)
>>>>>>> 115316dcff4362f71f7d83a83dc735e33e9750ed

import cv2
import cvlib
import math

def remove_blue(picture):
    """
    This function removes all the blue in each pixel in an image
    """
    image = cv2.imread(picture,1)
    picsize = (image.shape[0], image.shape[1])
    for px in range(picsize[0]):
        for py in range(picsize[1]):
            image[px,py][0] = 0

    cv2.imshow("Blue Eagle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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


def all_pairs_ordered(roof):
    out = [(x,y) for x in range(roof+1) for y in range (roof+1)]
    return out


def factorial (nr):
    """
    Earlier made function that we reuse that calculates the factorial of a
    number and is used in the function choose.
    """
    if nr < 1:
        return 1
    else:
        summa = nr * factorial(nr - 1)
    return summa


def delfactor (n, k):
    """
    Earlier made function that we reuse that calculates the factorial from n to
    k and is used in the function choose.
    """
    if n <= k:
        return 1
    else:
        return n * delfactor(n-1, k)


def choose(n, k):
    """
    Earlier mad function that we reuse that calculates n choose k and used the
    function factorial and the function delfactor.
    """
    if k >= (n-k):
        return delfactor(n, k)//factorial(n-k)
    else:
        return delfactor(n, n-k)//factorial(k)


def pascals(rows):
    """
    Function that calculates and returns a list of pascals triangle and uses the
    function choose.
    """
    out = [[choose(y, x) for x in range(y + 1)] for y in range(rows)]
    return out


<<<<<<< HEAD
def gaus(cord):
    """
    Calcualates the negativ gauss blue for the pixel cordinates sent in.
    """
    if cord[0] == 0 and cord[1] == 0:
        return 1.5
    else:
        s = 4.5
        x = cord[0]
        y = cord[1]
        exponent = -(((x**2)+(y**2))/(2*(s**2)))
        result = -((1)/(2*(math.pi)*(s**2)))*math.exp(exponent)
        return result


def dimension_converter(n):
    """
    Takes in the value of n and creates a tuple with the dimensions for
    our array and then creates an array with .
    """
    result = []
    var = 0
    for x in range(n):
        if x == 0:
            var += 1
            result.append(0)
        elif x % 2 != 0:
            neg = - var
            result.insert(0, neg)
        elif x % 2 == 0:
            result.append(var)
            var += 1

    utlist = []
    utlist = [[x,y] for x in result for y in result]
    return(utlist)


def unsharp_mask(n):
    """
    Increases the clarity in a picture and uses the funcions dimension_converter
    and gaus to do so.
    """
    dime = dimension_converter(n)
    gau = [[gaus(dime[x+y*n]) for x in range(n)] for y in range(n)]
    return gau
=======

<<<<<<< HEAD
def distribute(inlist):
    utlist = inlist.copy()
    [[utlist.append(inlist[elem]) for elem in range(len(inlist))] for ele in range(len(inlist))]
    return utlist


def create_lock(code,message):
    def lock(code2):
        if code == code2:
            print(message)
        else:
            print("Fel kod!")
    return lock


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
=======
>>>>>>> 792c8afc5cc08132f979d2bcf1555caf55b2eb75
>>>>>>> 115316dcff4362f71f7d83a83dc735e33e9750ed

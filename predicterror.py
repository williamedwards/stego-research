#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      William
#
# Created:     01/07/2013
# Copyright:   (c) William 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import scipy.ndimage as ndimg
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import math, time

def _errorImg(img,xoff,yoff,threshold):
    eimg = np.empty_like(img, dtype = np.dtype("int8"))
    for i, row in enumerate(img):
        if i < len(img) - 2:
            for j, p in enumerate(row):
                if j < len(row) - 2:
                    a = int(img[i+1][j])
                    b = int(img[i][j+1])
                    c = int(img[i+1][j+1])
                    if c <= a and c <= b:
                        if a > b:
                            pr = a
                        else:
                            pr = b
                    elif c >=a and c >=b:
                        if a < b:
                            pr = a
                        else:
                            pr = b
                    else:
                        pr = a + b -c
                    e = int(p) - pr
                    if math.fabs(e) > threshold and threshold != 0:
                        e = 0
                    eimg[i][j] = e
                else:
                    eimg[i][j] = 0
        else:
            for j in xrange(0,len(row)):
                eimg[i][j] = 0
    return eimg


def horz(img, threshold=0):
    return _errorImg(img,1,0,threshold)

def vert(img, threshold=0):
    return _errorImg(img,0,1,threshold)

def diag(img, threshold=0):
    return _errorImg(img,1,1,threshold)

def same(img, threshold=0):
    return img

def main():
    img = ndimg.imread("../images/li_photograph/image.cd/1/10000.jpg")
    imgr = img[:,:,0]
    imgg = img[:,:,1]
    imgb = img[:,:,2]
    p = 1
    for img in imgr, imgg, imgb:
        for func in same, horz, vert, diag:
            plt.subplot(3,4, p)
            plt.title(str(p))
            plt.imshow(func(img,threshold=4), cmap = cm.binary)
            p += 1
    plt.show()

if __name__ == '__main__':
    main()

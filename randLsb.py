#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      William
#
# Created:     23/09/2013
# Copyright:   (c) William 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random as random
import scipy.ndimage as ndimg
import numpy as np

def randLsb(oimg,rate):
    if rate == 0:
        return oimg
    img = np.empty_like(oimg)
    img[:] = oimg
    for i in xrange(0,len(img.flat)):
        if random.random() < rate:
            img.flat[i] ^= 0 if random.random() < 0.5 else 1
    return img

def rand(imname,r,flatten=False):
    return randLsb(np.uint8(ndimg.imread("../images/li_photograph/image.cd/" + imname[0] + "/" + imname + ".jpg", flatten=flatten)),r)

def main():
    img = ndimg.imread("../images/li_photograph/image.cd/1/10000.jpg")
    print (img == randLsb(img,1))

if __name__ == '__main__':
    main()

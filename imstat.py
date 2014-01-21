#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      William
#
# Created:     19/09/2013
# Copyright:   (c) William 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import statmethods as stm
import scipy.stats as st
import numpy as np
import scipy.ndimage as ndimg
import time, itertools, os
import randLsb

def checkpath(p):
    if not os.path.exists(os.path.dirname(p)):
        os.makedirs(os.path.dirname(p))

def getStats(img, methods):
##    imgr = img[:,:,0]
##    imgg = img[:,:,1]
##    imgb = img[:,:,2]
    stats = []
    for method in methods:
        stats += method(img)
    return stats

def writeStats(imname, savepath, img=None, overwrite=False, methods=[stm.predicterror2]):
    if not os.path.exists("../images/" + savepath + imname + ".npy") or overwrite:
        if img == None:
            p = "../images/li_photograph/image.cd/" + imname[0] + "/" + imname + ".jpg"
            checkpath(p)
            img = np.uint8(ndimg.imread(p, flatten=True))
        stats = getStats(img, methods)
        p = "../images/" + savepath + imname
        checkpath(p)
        np.save(p, stats)
        return stats

def loadStats(imlist, loadpath="../images/imstats/final02/"):
    n = len(np.load(loadpath + imlist[0] + ".npy"))
    stats = np.empty((len(imlist), n))
    for i, im in enumerate(imlist):
        stats[i] = np.load(loadpath + im + ".npy")
    return stats

def main():
    pass

if __name__ == '__main__':
    main()

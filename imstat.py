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

def getStats(img, methods):
##    imgr = img[:,:,0]
##    imgg = img[:,:,1]
##    imgb = img[:,:,2]
    eims = []
    for method in methods:
        eims.append(method(img))
    stats = []
    for eim in eims:
        stats += [s(eim, axis=None) for s in (np.mean, np.var,st.skew,st.kurtosis)]
    return stats

def writeStats(imname, savepath, img=None, overwrite=False, methods=[stm.predicterror2]):
    if not os.path.exists("../images/" + savepath + imname + ".npy") or overwrite:
        if img == None:
            img = np.uint8(ndimg.imread("../images/li_photograph/image.cd/" + imname[0] + "/" + imname + ".jpg", flatten=True))
        stats = getStats(img, methods)
        np.save("../images/" + savepath + imname, stats)
        return stats

def loadStats(imlist, loadpath="../images/imstats/final02/"):
    stats = np.empty((len(imlist), 8))
    for i, im in enumerate(imlist):
        stats[i] = np.load(loadpath + im + ".npy")
    return stats

def main():
    pass

if __name__ == '__main__':
    main()

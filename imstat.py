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

def getStats(img):
##    imgr = img[:,:,0]
##    imgg = img[:,:,1]
##    imgb = img[:,:,2]
    eim = stm.predicterror2(img)
    stats = [s(eim, axis=None) for s in (np.mean, np.var,st.skew,st.kurtosis)]
    return stats

def writeStats(imname, savepath, img=None, overwrite=False):
    if not os.path.exists("../images/" + savepath + imname + ".npy") or overwrite:
        if img == None:
            img = ndimg.imread("../images/li_photograph/image.cd/" + imname[0] + "/" + imname + ".jpg", flatten=True)
        np.save("../images/" + savepath + imname, getStats(img))



def main():
    pass

if __name__ == '__main__':
    main()

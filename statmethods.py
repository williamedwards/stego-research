#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      William
#
# Created:     10/11/2013
# Copyright:   (c) William 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np, scipy.stats as st, scipy.ndimage as ndimg, math, pywt

def same(img):
    return [s(img, axis=None) for s in (np.mean,np.var,st.skew,st.kurtosis)]

def predicterror1(img, threshold=4):
    #Produces three prediction error images based on Zou article
    #Horizontal, vertical, and diagonal error image
    #Returns Mean, Variance, Skewness, and Kurtosis for each
    stats = []
    for xoff, yoff in ((1,0),(0,1),(1,1)):
        eim = np.empty_like(img, dtype=np.dtype("int8"))
        for i, row in enumerate(img):
            if i < len(img) - yoff:
                for j, p in enumerate(row):
                    if j < len(row) - xoff:
                        eim[i,j] = int(img[i+yoff,j+xoff]) - int(img[i,j])
                        if math.fabs(eim[i,j]) >= threshold:
                            eim[i,j] = 0
                    else:
                        eim[i,j] = 0
            else:
                for j in xrange(0,len(row)):
                    eim[i,j] = 0
        stats += [s(eim,axis=None) for s in (np.mean,np.var,st.skew,st.kurtosis)]
    return stats

def predicterror2(img, raw_image=False):
    #Produces a single prediction error image based on Shi article
    #Returns Mean, Variance, Skewness, and Kurtosis for each
    eim = np.empty_like(img)
    for i, row in enumerate(img):
        if i < len(img) -1:
            for j, p in enumerate(row):
                if j < len(row) - 1:
                    a = img[i+1, j]
                    b = img[i, j+1]
                    c = img[i+1, j+1]
                    if c <= min(a,b):
                        pr = max(a,b)
                    elif c >= max(a,b):
                        pr = min(a,b)
                    else:
                        pr = int(a) + int(b) - int(c)
                    eim[i,j] = pr - int(p)
                else:
                    eim[i,j] = 0
        else:
            for j, p in enumerate(row):
                eim[i,j] = 0
    if not raw_image:
        return [s(eim,axis=None) for s in (np.mean,np.var,st.skew,st.kurtosis)]
    else:
        return eim

def haar(img, level=1):
    #Calculates a discrete wavelet transform based on the Haar wavelet
    #Calculates mean, variance, skewness, kurtosis based on each of four wavelet subbands
    dwt = pywt.wavedec2(img, "haar", level=level)
    cs = [dwt[0]]
    for c in dwt[1:]:
        cs += c
    return [s(c, axis=None) for c in cs for s in np.mean, np.var, st.skew, st.kurtosis]

if __name__ == "__main__":
    print haar(ndimg.imread("../images/li_photograph/image.cd/1/10000.jpg")[:,:,0])
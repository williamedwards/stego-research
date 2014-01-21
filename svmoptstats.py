#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      William
#
# Created:     16/12/2013
# Copyright:   (c) William 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy, imstat, randLsb, selector, statmethods as stm, os

TRIALS = 100
kernel = "linear"
RUN=4

def checkpath(p):
    if not os.path.exists(os.path.dirname(p)):
        os.makedirs(os.path.dirname(p))

def main():
    methods = [stm.same, stm.predicterror2, lambda x: stm.haar(x, level=3), lambda x: stm.haar(stm.predicterror2(x, raw_image=True), level=3)]
    
    clearlist = selector.select(TRIALS)
    path = "../data/svmopt/" + str(RUN) +'/lists/' + kernel + '/' + "clear.txt"
    checkpath(path)
    file = open(path, "w")
    file.write(','.join(clearlist))
    file.close
    for im in clearlist:
        imstat.writeStats(im, "imstats/svmopt/" + str(RUN) + "/" + kernel + "/clear/", img=randLsb.rand(im, 0, flatten=True), methods=methods)
    print "Clear Done"
    
    for rate in [0.01, 0.05, 0.1, 0.5, 0.8, 1.0]:
        stegolist = selector.select(TRIALS)
        path = "../data/svmopt/" + str(RUN) +'/lists/' + kernel + '/' + str(int(rate*100)) + ".txt"
        checkpath(path)
        file = open(path, "w")
        file.write(','.join(stegolist))
        file.close
        for im in stegolist:
            imstat.writeStats(im, "imstats/svmopt/" + str(RUN) + "/" + kernel + "/" + str(int(rate*100)) + "/", img=randLsb.rand(im, rate, flatten=True), methods=methods)
        print str(rate) + " Done"

if __name__ == '__main__':
    main()

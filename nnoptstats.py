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
RUN=1

def checkpath(p):
    if not os.path.exists(os.path.dirname(p)):
        os.makedirs(os.path.dirname(p))

def main():
    methods = [stm.same, stm.predicterror2, lambda x: stm.haar(x, level=3), lambda x: stm.haar(stm.predicterror2(x, raw_image=True), level=3)]
    
    clearlist = selector.select(TRIALS)
    path = "../data/nnopt/" + str(RUN) +'/lists/' + "clear.txt"
    checkpath(path)
    file = open(path, "w")
    file.write(','.join(clearlist))
    file.close
    for im in clearlist:
        imstat.writeStats(im, "imstats/nnopt/" + str(RUN) + "/clear/", img=randLsb.rand(im, 0, flatten=True), methods=methods)
    print "Clear Done"
    
    for rate in [.01,.05,.1,.2,.3,.5,.8,1.0]:
        stegolist = selector.select(TRIALS)
        path = "../data/nnopt/" + str(RUN) +'/lists/' + str(int(rate*100)) + ".txt"
        checkpath(path)
        file = open(path, "w")
        file.write(','.join(stegolist))
        file.close
        for im in stegolist:
            imstat.writeStats(im, "imstats/nnopt/" + str(RUN) + "/" + str(int(rate*100)) + "/", img=randLsb.rand(im, rate, flatten=True), methods=methods)
        print str(rate) + " Done"

if __name__ == '__main__':
    main()

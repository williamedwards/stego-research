#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     
#
# Author:      William
#
# Created:     25/01/2014
# Copyright:   (c) William 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import selector, imstat, os, statmethods as stm, randLsb
RUN = 2
TrainSize = 100
EvalSize = 100
methods = [stm.same, stm.predicterror2, lambda x: stm.haar(x, level=3), lambda x: stm.haar(stm.predicterror2(x, raw_image=True), level=3)]

def checkpath(p):
    if not os.path.exists(os.path.dirname(p)):
        os.makedirs(os.path.dirname(p))
        
def main():
    # Generate Statistics for the Training Set
    # First generate clear images:
    clearlist = selector.select(TrainSize)
    path = "../data/final/" + str(RUN) + "/lists/tclear.txt"
    checkpath(path)
    file = open(path, "w")
    file.write(",".join(clearlist))
    file.close()
    for im in clearlist:
        imstat.writeStats(im, "imstats/final/" + str(RUN) + "/tclear/", img=randLsb.rand(im, 0, flatten=True), methods=methods)
    print "Done Clear Training"
    # Next Generate stego-images
    for rate in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5]:
        stegolist = selector.select(TrainSize)
        path = "../data/final/" + str(RUN) + "/lists/t" + str(int(rate*100)) + ".txt"
        checkpath(path)
        file = open(path, "w")
        file.write(",".join(stegolist))
        file.close()
        for im in stegolist:
            imstat.writeStats(im, "imstats/final/" + str(RUN) + "/t" + str(int(rate*100)) + "/", img=randLsb.rand(im, rate, flatten=True), methods=methods)
        print "Done Stego Eval " + str(rate) 
    
    #Now for the Eval Sets
    clearlist = selector.select(EvalSize)
    path = "../data/final/" + str(RUN) + "/lists/eclear.txt"
    checkpath(path)
    file = open(path, "w")
    file.write(",".join(clearlist))
    file.close()
    for im in clearlist:
        imstat.writeStats(im, "imstats/final/" + str(RUN) + "/eclear/", img=randLsb.rand(im, 0, flatten=True), methods=methods)
    print "Done Clear Eval"
    
    for rate in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5]:
        stegolist = selector.select(EvalSize)
        path = "../data/final/" + str(RUN) + "/lists/e" + str(int(rate*100)) + ".txt"
        checkpath(path)
        file = open(path, "w")
        file.write(",".join(stegolist))
        file.close()
        for im in stegolist:
            imstat.writeStats(im, "imstats/final/" + str(RUN) + "/e" + str(int(rate*100)) + "/", img=randLsb.rand(im, rate, flatten=True), methods=methods)
        print "Done Stego Eval " + str(rate)   

if __name__ == '__main__':
    main()

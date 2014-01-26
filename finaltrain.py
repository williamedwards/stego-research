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
from sklearn import preprocessing, svm
import imstat, numpy as np, cPickle, nnwrapper, os, copy
RUN = 1
# Set Parameters:
params = {}
params["linear"] = {"C":0.1, "kernel":"linear"}
params["rbf"] = {"C":10,"gamma":.001, "kernel":"rbf"}
params["ann"] = {"hlayers":3,"hnodes":40, "lrate":0.1}

def checkpath(p):
    if not os.path.exists(os.path.dirname(p)):
        os.makedirs(os.path.dirname(p))
        
def main():
    file = open("../data/final/" + str(RUN) + "/lists/tclear.txt", "r")
    clearlist = file.read().split(",")
    file.close()
    file = open("../data/final/" + str(RUN) + "/lists/tstego.txt", "r")
    stegolist = file.read().split(",")
    file.close()
    clearstats = imstat.loadStats(clearlist, loadpath="../images/imstats/final/" + str(RUN) + "/tclear/")
    stegostats = imstat.loadStats(stegolist, loadpath="../images/imstats/final/" + str(RUN) + "/tstego/")
    dataset = np.concatenate((clearstats,stegostats))
    preprocessing.scale(dataset)
    target = np.asarray([0 for j in clearlist] + [1 for j in stegolist])
    print target
    
##    #First the Support Vector Machines
##    for kernel in ("linear","rbf"):
##        svc = svm.SVC(**params[kernel])
##        svc.fit(dataset,target)
##        path = "../pickles/final/" + str(RUN) + "/" + str(kernel)
##        checkpath(path)
##        file = open(path, "w")
##        cPickle.dump(svc,file)
##        file.close()
        
    #Now the neural network
    ann = nnwrapper.ANN(**params["ann"])
    ann.train = lambda b: b.trainUntilConvergence()
    ann.fit(dataset, target)
    ann2 = nnwrapper.ANN(**params["ann"])
    ann2.net = copy.deepcopy(ann.net)
    path = "../pickles/final/" + str(RUN) + "/ann"
    checkpath(path)
    file=open(path, "w")
    cPickle.dump(ann2,file)
    file.close()

if __name__ == '__main__':
    main()

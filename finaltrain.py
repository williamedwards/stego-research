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
RUN = 2
# Set Parameters:
params = {}
params["linear"] = {.01:{"C":1},.05:{"C":100},.1:{"C":0.01},.2:{"C":10},.3:{"C":0.1},.5:{"C":0.1}}

params["rbf"] = {.01:{"C":1,"gamma":.1, "kernel":"rbf"},.05:{"C":1000,"gamma":.0001, "kernel":"rbf"},.1:{"C":10,"gamma":.001, "kernel":"rbf"},
.2:{"C":10,"gamma":.001, "kernel":"rbf"},.3:{"C":10,"gamma":.01, "kernel":"rbf"}, .5:{"C":10,"gamma":.001, "kernel":"rbf"}} 
    
params["ann"] = {.01:{"hlayers":3,"hnodes":60, "lrate":0.1},.05:{"hlayers":2,"hnodes":10, "lrate":10},.1:{"hlayers":3,"hnodes":30, "lrate":1},.2:{"hlayers":3,"hnodes":30, "lrate":1},
.3:{"hlayers":3,"hnodes":10, "lrate":100},.5:{"hlayers":3,"hnodes":40, "lrate":0.1}}

def checkpath(p):
    if not os.path.exists(os.path.dirname(p)):
        os.makedirs(os.path.dirname(p))
        
def main():
    file = open("../data/final/" + str(RUN) + "/lists/tclear.txt", "r")
    clearlist = file.read().split(",")[0:50]
    file.close()
    clearstats = imstat.loadStats(clearlist, loadpath="../images/imstats/final/" + str(RUN) + "/tclear/")
    for rate in [.01,0.05,0.1,0.2,0.3,0.5]:
        file = open("../data/final/" + str(RUN) + "/lists/t" + str(int(rate*100)) + ".txt", "r")
        stegolist = file.read().split(",")[0:50]
        file.close()
        stegostats = imstat.loadStats(stegolist, loadpath="../images/imstats/final/" + str(RUN) + "/t" + str(int(rate*100)) + "/")
        dataset = np.concatenate((clearstats,stegostats))
        preprocessing.scale(dataset)
        target = np.asarray([0 for j in clearlist] + [1 for j in stegolist])
        #First the Support Vector Machines
        for kernel in ("rbf","linear"):
            if kernel == "linear":
                svc = svm.LinearSVC(**params[kernel][rate])
            else:
                svc = svm.SVC(**params[kernel][rate])
            svc.fit(dataset,target)
            path = "../pickles/final/" + str(RUN) + "/" + str(kernel) + str(int(rate*100))
            checkpath(path)
            file = open(path, "w")
            cPickle.dump(svc,file)
            file.close()
            
        #Now the neural network
        ann = nnwrapper.ANN(**params["ann"][rate])
        ann.train = lambda b: b.trainUntilConvergence(maxEpochs=50)
        ann.fit(dataset, target)
        ann2 = nnwrapper.ANN(**params["ann"][rate])
        ann2.net = copy.deepcopy(ann.net)
        path = "../pickles/final/" + str(RUN) + "/ann" + str(int(rate*100))
        checkpath(path)
        file=open(path, "w")
        cPickle.dump(ann2,file)
        file.close()

if __name__ == '__main__':
    main()

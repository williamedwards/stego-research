#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      William
#
# Created:     15/12/2013
# Copyright:   (c) William 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np, selector, imstat, randLsb, time, nnwrapper
from sklearn import preprocessing, grid_search
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score

RUN = 1

def main():
    stime = time.time()
    file = open("../data/nnopt/" + str(RUN) + "/lists/clear.txt", "r")
    clearlist = file.read().split(",")
    clearstats = imstat.loadStats(clearlist, loadpath="../images/imstats/nnopt/" + str(RUN) + "/clear/")
    file.close()

    for i, rate in enumerate([0.01,0.05,0.1,0.2,0.3,0.5,0.8,1.0]):
        file = open("../data/nnopt/" + str(RUN) +'/lists/' + str(int(rate*100)) + ".txt", "r")
        stegolist = file.read().split(",")
        file.close()
        stegostats = imstat.loadStats(stegolist, loadpath="../images/imstats/nnopt/" + str(RUN) + "/" + str(int(rate*100)) + "/")
        optset = np.concatenate((clearstats, stegostats))
        optset = preprocessing.scale(optset)
        nn = nnwrapper.ANN()
        param_grid = {"hlayers":[1,2,3],"hnodes":[i for i in xrange(10,160,10)],"lrate":[10**k for k in xrange(-3,3)]}
        clf = grid_search.GridSearchCV(nn, param_grid, cv=5, scoring="accuracy")
        clf.fit(optset, [0 for j in clearlist] + [1 for j in stegolist])
        print clf.best_params_
        print clf.best_score_
    print time.time() - stime


if __name__ == '__main__':
    main()

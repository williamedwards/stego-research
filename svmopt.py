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
import numpy as np, selector, imstat, randLsb, time
from sklearn import preprocessing, grid_search, svm
from sklearn.metrics import jaccard_similarity_score
from matplotlib import pyplot as plt

RUN = 4
kernel = "rbf"

def main():
    stime = time.time()
    file = open("../data/svmopt/" + str(RUN) +'/lists/' + kernel + '/' + "clear.txt", "r")
    clearlist = file.read().split(",")
    clearstats = imstat.loadStats(clearlist, loadpath="../images/imstats/svmopt/" + str(RUN) + "/" + kernel + "/clear/")
    file.close()

    for i, rate in enumerate([.01,.05,.10,.20,0.30,0.50,.80,1.00]):
        file = open("../data/svmopt/" + str(RUN) +'/lists/' + kernel + '/' + str(int(rate*100)) + ".txt", "r")
        stegolist = file.read().split(",")
        file.close()
        stegostats = imstat.loadStats(stegolist, loadpath="../images/imstats/svmopt/" + str(RUN) + "/" + kernel + "/" + str(int(rate*100)) + "/")
        optset = np.concatenate((clearstats, stegostats))
        plt.plot(clearstats[:,1],clearstats[:,15], "bo")
        plt.plot(stegostats[:,1],stegostats[:,15], "r+")
        plt.show()
##        optset = preprocessing.scale(optset)
##        svr = svm.SVC(kernel=kernel)
##        param_grid = {"C":[10**k for k in xrange(-6,5)] , "gamma":[10**k for k in xrange(-6,5)]}
##        clf = grid_search.GridSearchCV(svr, param_grid, cv=5, scoring="accuracy")
##        clf.fit(optset, np.asarray([0 for j in clearlist] + [1 for j in stegolist]))
##        print clf.best_params_
##        print clf.best_score_
##    print time.time() - stime

if __name__ == '__main__':
    main()

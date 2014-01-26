#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     
#
# Author:      William
#
# Created:     26/01/2014
# Copyright:   (c) William 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import imstat, cPickle
RUN = 1

def main():
    correct = {}
    file = open("../data/final/" + str(RUN) + "/lists/eclear.txt")
    clearlist = file.read().split(",")
    file.close()
    clearstats = imstat.loadStats(clearlist, loadpath="../images/imstats/final/" + str(RUN) + "/eclear/")
    correct[0] = test(clearstats, 0)
    
    for rate in [0.01,0.05,0.1,0.2,0.3,0.5]:
        file = open("../data/final/" + str(RUN) + "/lists/e" + str(int(rate*100)) + ".txt")
        stegolist = file.read().split(",")
        file.close()
        stegostats = imstat.loadStats(stegolist, loadpath="../images/imstats/final/" + str(RUN) + "/e" + str(int(rate*100)) + "/")
        correct[rate] = test(stegostats,1)
    print correct

def test(stats, expected):
    estimators = []
    correct = {}
    for name in "linear","rbf","ann":
        file = open("../pickles/final/" + str(RUN) + "/" + name, "r")
        est = cPickle.load(file)
        file.close()
        correct[name] = 0
        results = est.predict(stats)
        for result in results:
            correct[name] += int(result == expected)
    return correct
        
            

if __name__ == '__main__':
    main()

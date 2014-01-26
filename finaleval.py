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
RUN = 2

def main():
    correctc = {}
    corrects = {}
    data=[]
    data
    file = open("../data/final/" + str(RUN) + "/lists/eclear.txt")
    clearlist = file.read().split(",")
    file.close()
    clearstats = imstat.loadStats(clearlist, loadpath="../images/imstats/final/" + str(RUN) + "/eclear/")
    
    for rate in [0.01,0.05,0.1,0.2,0.3,0.5]:
        file = open("../data/final/" + str(RUN) + "/lists/e" + str(int(rate*100)) + ".txt")
        stegolist = file.read().split(",")
        file.close()
        stegostats = imstat.loadStats(stegolist, loadpath="../images/imstats/final/" + str(RUN) + "/e" + str(int(rate*100)) + "/")
        correctc[rate], cresults = test(clearstats,0, str(int(rate*100)))
        corrects[rate], sresults = test(stegostats,1, str(int(rate*100)))
        for name in cresults:
            for res, im in zip(cresults[name], clearlist):
                data.append({"Image":im, "Estimator":name, "Rate":str(rate), "Type":"Clear", "Success":str(res)})
        for name in sresults:
            for res, im in zip(sresults[name], stegolist):
                data.append({"Image":im, "Estimator":name, "Rate":str(rate), "Type":"Stego", "Success":str(res)})
    datastring = "\t".join(data[0].keys()) + "\n"
    for i, datum in enumerate(data):
        datastring += "\t".join(data[i].values()) + "\n"
    p = "../data/final/" + str(RUN) + "/data.txt"
    imstat.checkpath(p)
    file = open(p, "w")
    file.write(datastring)
    file.close()
            
    print correctc
    print corrects

def test(stats, expected, suffix):
    estimators = []
    correct = {}
    results = {}
    for name in "linear","rbf","ann":
        file = open("../pickles/final/" + str(RUN) + "/" + name + suffix, "r")
        est = cPickle.load(file)
        file.close()
        correct[name] = 0
        results[name] = est.predict(stats)
        for result in results[name]:
            print result
            print expected
            print int(result == expected)
            correct[name] += int(result == expected)
    return correct, results
        
            

if __name__ == '__main__':
    main()

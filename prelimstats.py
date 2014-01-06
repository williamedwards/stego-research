#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      William
#
# Created:     10/11/2013
# Copyright:   (c) William 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import selector, randLsb, scipy.ndimage as ndimg, statmethods as stm, time
RUN = 4
methods = [stm.same, stm.predicterror1, stm.predicterror2, lambda im: stm.haar(im, level=3)]
methodnames = ['same','PE1','PE2','Haar']

def main():
    stime = time.time()
    imlist = selector.select(100)
    file = open("../data/prelimstats/%u/imlist.txt" % RUN, "w")
    file.write(",".join(imlist))
    file.close()

#-------------------------------------------------
#Format for statistics array
#[image index][statistic][moment]
#-------------------------------------------------

    statsclear = []
    for i, imname in enumerate(imlist):
        img = ndimg.imread("../images/li_photograph/image.cd/" + imname[0] + "/" + imname + ".jpg", flatten=True)
        statsclear.append([])
        for m in methods:
            statsclear[i].append(m(img))
        print i

    statsstego = []
    for i, imname in enumerate(imlist):
        img = randLsb.rand(imname, 1.0, flatten=True)
        statsstego.append([])
        for m in methods:
            statsstego[i].append(m(img))
        print i

    #Write data to file:

    datastring = "Image\tMethod\tMoment\tClear\tStego\n"
    for i, imname in enumerate(imlist):
        #for j, color in enumerate(('R','G','B')):
            for k, stat in enumerate(methodnames):
                if stat == "Haar":
                    for m, stat2 in enumerate(('cA3','cH3','cD3','cV3', 'cH2','cD2','cV2', 'cH1','cD1','cV1')):
                        for l, moment in enumerate(("mean","var","skew","kurt")):
                            datastring += "%s\t%s\t%s\t%s\t%s\n" % (imname, stat2, moment,  str(statsclear[i][k][l + 4*m]), str(statsstego[i][k][l + 4*m]))
                elif stat == "PE1":
                    for m, stat2 in enumerate(('peH','peV','peD')):
                        for l, moment in enumerate(("mean","var","skew","kurt")):
                            datastring += "%s\t%s\t%s\t%s\t%s\n" % (imname, stat2, moment,  str(statsclear[i][k][l + 4*m]), str(statsstego[i][k][l + 4*m]))
                else:
                    for l, moment in enumerate(("mean","var","skew","kurt")):
                        datastring += "%s\t%s\t%s\t%s\t%s\n" % (imname, stat, moment,  str(statsclear[i][k][l]), str(statsstego[i][k][l]))
    file = open("../data/prelimstats/%u/data.txt" % RUN, "w")
    file.write(datastring)
    file.close()

    print time.time() - stime
if __name__ == '__main__':
    main()

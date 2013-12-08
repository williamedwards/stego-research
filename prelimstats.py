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
RUN = 3
methods = [stm.same, stm.predicterror1, stm.predicterror2, stm.haar]
methodnames = ['same','PE1','PE2','Haar']

def main():
    stime = time.time()
    imlist = selector.select(100)
    file = open("../data/prelimstats/%u/imlist.txt" % RUN, "w")
    file.write(",".join(imlist))
    file.close()

#-------------------------------------------------
#Format for statistics array
#[image index][color channel][statistic][moment]
#-------------------------------------------------

    statsclear = []
    for i, imname in enumerate(imlist):
        img = ndimg.imread("../images/li_photograph/image.cd/" + imname[0] + "/" + imname + ".jpg", flatten=True)
        statsclear.append([[],[],[]])
        for j in xrange(0,1):
            im = img[:,:]
            for m in methods:
                statsclear[i][j].append(m(im))

    statsstego = []
    for i, imname in enumerate(imlist):
        img = randLsb.rand(imname, 1.0)
        statsstego.append([[],[],[]])
        for j in xrange(0,1):
            im = img[:,:,j]
            for m in methods:
                statsstego[i][j].append(m(im))

    #Write data to file:

    datastring = "Image\tMethod\tMoment\tClear\tStego\n"
    for i, imname in enumerate(imlist):
        #for j, color in enumerate(('R','G','B')):
            for k, stat in enumerate(methodnames):
                if stat == "Haar":
                    for m, stat2 in enumerate(('cA','cH','cD','cV')):
                        for l, moment in enumerate(("mean","var","skew","kurt")):
                            datastring += "%s\t%s\t%s\t%s\t%s\n" % (imname, stat2, moment,  str(statsclear[i][j][k][l + 4*m]), str(statsstego[i][j][k][l + 4*m]))
                elif stat == "PE1":
                    for m, stat2 in enumerate(('peH','peV','peD')):
                        for l, moment in enumerate(("mean","var","skew","kurt")):
                            datastring += "%s\t%s\t%s\t%s\t%s\n" % (imname, stat2, moment,  str(statsclear[i][j][k][l + 4*m]), str(statsstego[i][j][k][l + 4*m]))
                else:
                    for l, moment in enumerate(("mean","var","skew","kurt")):
                        datastring += "%s\t%s\t%s\t%s\t%s\n" % (imname, stat, moment,  str(statsclear[i][j][k][l]), str(statsstego[i][j][k][l]))
    file = open("../data/prelimstats/%u/data.txt" % RUN, "w")
    file.write(datastring)
    file.close()

    print time.time() - stime
if __name__ == '__main__':
    main()

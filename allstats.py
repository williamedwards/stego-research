#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      William
#
# Created:     13/12/2013
# Copyright:   (c) William 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import selector, imstat, time

def main():
    stime=time.time()
    i=0
    for im in selector.select(-1):
        imstat.writeStats(im, "imstats/final02/")
        print(str(i) + "\t" + str(time.time()-stime))
        i += 1

if __name__ == '__main__':
    main()

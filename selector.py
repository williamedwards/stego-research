#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      William
#
# Created:     03/10/2013
# Copyright:   (c) William 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
from itertools import chain
import numpy as np
import os
p = "../images/li_photograph/image.cd/"
k = filter(lambda a: a != "Thumbs.db", (os.listdir(p + "1/") + os.listdir(p + "2/") + os.listdir(p + "3/") + os.listdir(p + "4/") + os.listdir(p + "5/")))

def select(n):
    l = [i.rstrip(".jpg") for i in random.sample(k,n)]
    return l

def main():
    print select(30,2)

if __name__ == '__main__':
    main()

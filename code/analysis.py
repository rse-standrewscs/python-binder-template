#!/usr/bin/env python

import sys
import numpy

def row_means(datafile):
    data = numpy.loadtxt(datafile, delimiter=',')
    for row_mean in numpy.mean(data, axis=1):
        print(row_mean)


def main():
    if len(sys.argv) != 2:
        print("Usage: analysis.py <datafile>") 
    else:  
        row_means(sys.argv[1])

if __name__ == '__main__':
   main()

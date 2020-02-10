#!/usr/bin/env python

import sys
import numpy

def main():
    if len(sys.argv) != 2:
        print("Usage: analysis.py <datafile>") 
    else:  
        data = numpy.loadtxt(sys.argv[1], delimiter=',')
        for row_mean in numpy.mean(data, axis=1):
            print(row_mean)

if __name__ == '__main__':
   main()

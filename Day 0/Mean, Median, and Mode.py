#!/bin/python3

import statistics 
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))
    s.sort()

    print(statistics.mean(s))
    print(statistics.median(s))
    print(statistics.mode(s))  

    


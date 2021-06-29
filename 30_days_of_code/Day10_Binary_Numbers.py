#Task
#Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base- 10 integer denoting the maximum number of 
# consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript. 


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary=list(bin(n)[2:])
    count=0
    max_c=0
    for i in binary:
        if(i=='1'):
            count=count+1
        else:
            if count>max_c:
                max_c=count
            count=0
    if count>max_c:
        max_c=count
    print(max_c)
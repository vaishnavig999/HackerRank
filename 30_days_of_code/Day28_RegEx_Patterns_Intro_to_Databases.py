#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    a=[]
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
       
        if emailID[-10:] == '@gmail.com' :
             a.append(firstName)
    a.sort()
    for i in range(len(a)):
        print(a[i])

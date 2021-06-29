# #Context
# #Given a 6x6 2D Array,A:

# #1 1 1 0 0 0
# #0 1 0 0 0 0
# #1 1 1 0 0 0
# #0 0 0 0 0 0
# #0 0 0 0 0 0
# #0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

# a b c
#   d
# e f g

# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

# Task
# Calculate the hourglass sum for every hourglass in Athen print the maximum hourglass sum.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    max = 0

    for i in range(0,4):
        for j in range(0,4):
            sum = 0
            sum= arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if i==0 and j==0:
                max = sum
            if sum > max:
                max =sum

    print(max)

                                                                                                                                                                                                                                                                                                                                                                                                                  
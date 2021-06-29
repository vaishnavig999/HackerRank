# The absolute difference between two integers, a and b, is written as |a-b|. The maximum absolute difference 
# between two integers in a set of positive integers, elements, is the largest absolute difference between any two 
# integers in __elements.The Difference class is started for you in the editor. It has a private integer array (elements) 
# for storing N non-negative integers, and a public integer (maximumDifference) for storing the maximum absolute difference.

# Task
# Complete the Difference class by writing the following:
# A class constructor that takes an array of integers as a parameter and saves it to the __elements instance variable.
# A computeDifference method that finds the maximum absolute difference between any 2 numbers in __elements and 
# stores it in the maximumDifference instance variable. 

class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    
    def computeDifference(self):
        maximum=0
        
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                absdiff = abs(self.__elements[i] - self.__elements[j])
                if absdiff > maximum:
                    maximum = absdiff
        self.maximumDifference = maximum
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
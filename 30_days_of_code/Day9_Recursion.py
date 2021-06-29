
#Function Description
#Complete the factorial function in the editor below. Be sure to use recursion.factorial has the following paramter:

#int n: an integer
#Returns int: the factorial of n.

import os


def factorial(n):
    # Write your code here
    if n==1:
        return n
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

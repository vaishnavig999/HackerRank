# A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
# Given a number, n,determine and print whether it is Prime or Not prime.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
def prime(n):
    if n is 1:
        return "Not prime"
    for i in range(2,int(sqrt(n))+1):
        if n%i is 0:
            return "Not prime"
    return "Prime"
         

t = int(input())
for i in range(t):
    n = int(input())
    print(prime(n))

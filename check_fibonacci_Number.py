# check if a given number is a fibonacci number

import math
def isPerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s==x

# returns true if n is a Fibonacci number, else false
def isFibo(n):
    # n is afibonacci number if one of the 5*n*n+4 or 5*n*n-4 or both is aperfect square
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)

for i in range(1,11):
    if (isFibo(i)==True):
        print(i,'is a Fibonacci number')
    else:
        print(i,' is not a Fibonacci number')
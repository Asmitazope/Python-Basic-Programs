'''# 1 Recursive Approach
def fact(n):
    return 1 if(n==1 or n==0) else n*fact(n-1);

num=5
print("Factorial of",num, "is", fact(num))

#2 Iterative Approch

def fact(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while(n>1):
            fact=fact*n
            n=n-1
        return fact

num=6
print("Factorial of ", num,"is:",fact(num))

#3 method 3
def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact
num=int(input("Enter the number:"))

print("Fcatorial of ",num,"is:",factorial(num))


# 4 using in-built function
import math
def factorial(n):
    return math.factorial(n)

num=5
print("Fcatorial of ",num,"is:",factorial(num))

'''


def factorial(number):
    factorial = 1
    if number <= 0:
        return 1
    else:
        for i in range(2, number + 1):
            factorial = factorial * i

    return factorial

print("factorial: ", factorial(0))
print("factorial: ", factorial(1))
print("factorial: ", factorial(2))
print("factorial: ", factorial(3))
print("factorial: ", factorial(4))
print("factorial: ", factorial(5))
print("factorial: ", factorial(6))
print("factorial: ", factorial(7))
print("factorial: ", factorial(8))
print("factorial: ", factorial(9))



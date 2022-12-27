'''# Function for nth Fibonacci series
def fibonacci(n):
    if n<0:
        print('Incorrect input')
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))

# function for nth fibonacci using dynamic programming

Fibarray=[0,1]

def Fibonacci(n):
    if(n<0):
        print('Incorrect input')
    elif n<=len(Fibarray):
        return Fibarray[n-1]
    else:
        temp_fib=Fibonacci(n-1)+Fibonacci(n-2)
        Fibarray.append(temp_fib)
        return temp_fib
print(Fibonacci(20))

# function for nth fibonacci series space optimization
def Fibo(n):
    a=0
    b=1
    if n<0:
        print('Incorrect Number')
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return b
    
print('Fibonacci series:',Fibo(10))



'''
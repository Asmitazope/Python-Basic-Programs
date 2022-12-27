def fibonacci(n):
    if n<0:
        print('Incorrect Input')
    data=[0,1]
    if n>0:
        for i in range(2,n):
            data.append(data[i-1]+data[i-2])
    return data[n-1]

print(fibonacci(9))




from math import sqrt
def nth_Fibo(n):
    res=(((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
    print(int(res),'is',str(n)+'th Fibonacci number')

nth_Fibo(20)
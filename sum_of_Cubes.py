#1 method 1

def sum_of_Cubes(n):
    sum1=0

    for i in range(1,n+1):
        sum1=sum1+(i*i*i)
    return sum1
n=5
print(sum_of_Cubes(n))


#2 method 2 using 'pow' method

n=6
s=0

for i in range(1,n+1):
    s=s+pow(i,3)
print(s)
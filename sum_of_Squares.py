# 1 
def sum_of_Squares(n):
    sum1=0

    for i in range(1,n+1):
        sum1=sum1+(i*i)

    return sum1
n=10
print(sum_of_Squares(n))



#2
def squares_sum(n):
    return (n*(n+1)*(2*n+1))//6

n=4
print(squares_sum(n))



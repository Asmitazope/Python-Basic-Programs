n=153
temp=n
sum1=0
#b=len(str(n))

while n!=0:
    res=n%10
    sum1=sum1+res #(res*res*res)
    n=n//10
print(sum1)
if temp==sum1:
    print(temp,'is Armstrong number')
else:
    print(temp,'is not Armstrong number')
    
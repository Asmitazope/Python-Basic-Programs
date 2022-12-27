n=1221
temp=n
rev=0

while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)
if temp==rev:
    print(rev, ' is a pallindrome number')
else:
    print(rev, 'is not a pallindrome number')
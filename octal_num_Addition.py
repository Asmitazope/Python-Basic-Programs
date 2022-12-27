'''#1 octal sum
a='123'
b='456'

sum=oct(int(a,8)+int(b,8))

print(sum[2:])


#2 Driver code
if __name__=="__main__":
    a='732'
    b='465'

    octal_Sum= lambda a,b : oct(int(a,8)+int(b,8))

    print(octal_Sum(a,b)[2:])
'''
#3 using add operator

from operator import*
a='123'
b='234'
print(oct(add(int(a,8),int(b,8))))
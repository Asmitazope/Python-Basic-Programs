#1 using if-elif
a,b,c=4,6,2

if a>=b and a>=c:
    print(a,'is maximum')
elif b>=a and b>=c:
    print(b,'is maximum')
else:
    print(c,'is maximum')


#2 using max
print(max(a,b,c))
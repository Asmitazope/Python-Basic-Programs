'''#1 find maximum and minimum of two numbers
 
a=5
b=6

if a>b:
    print(a,"is maximum and", b, "is minimum")
else:
    print(b,"is maximum and", a, "is minimum")

print("\r")
#2 using max function

a=3
b=5

maxm=max(a,b)

print(maxm)
print("\r")
#3 creating a function

def maximum(a,b):
    if a>b :
        return a
    else:
        return b

a,b=8,9

print(maximum(a,b))
'''
#4 using lambda 

a=4;b=8

maximum=lambda a,b: a if a>b else b

print(f'{maximum(a,b)} is maximum number')

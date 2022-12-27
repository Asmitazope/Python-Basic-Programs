#1 using hex method

a='01B'
b='3AA'

sum=hex(int(a,16)+int(b,16))

print(sum[2:])


#2 driver code

a='AAC'
b='445'

hex_sum=lambda a,b:hex(int(a,16)+int(b,16))

print(hex_sum(a,b)[2:])

#3 using operator

from operator import*
a='CBA'
b='ABC'

print(hex(add(int(a,16),int(b,16))))
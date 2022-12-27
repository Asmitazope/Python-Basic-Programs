num=int(input('Enter the number:'))
#define flag variable
flag=False

# chaeck iif number is greater than 1
if num>1:
    # check for factors
    for i in range(2,num):
        if (num%i)==0:
            # if factor is found, set flag to true
            flag=True

            # break out of loop
            break

# check if flag is True

if flag:
    print(num,'is not a prime number')
else:
    print(num,'is a prime number')


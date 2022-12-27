def prime(x,y):
    prime_list=[]
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j==0:
                    break
            else:
                prime_list.append(i)
    return prime_list

start=int(input("Enter the starting range:"))
end=int(input("Enter the Ending Range:"))
lst=prime(start,end)

if(len(lst)==0):
    print('There are no prime numbers in this range')
else:
    print('The prime numbers in',start,end,'is:',lst)
'''
for i in range(start,end):
    for j in range(0,i+1):
        print(lst[i],end=' ')
    print('\r')'''
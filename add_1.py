#1 program to add two numbers

num1=10
num2=20
sum=num1+num2

print("Sum of {0} and {1} is :".format(num1,num2),sum, end=' ')

#2 integer addition using user input

num1=int(input("Enter number 1:"))
num2=int(input("\r Enter number 2:"))

sum= num1 + num2

print("Sum of {0} and {1} is :".format(num1,num2),sum)

#3 add two numbers drivers code

if __name__=="__main__":
    num1=10
    num2=20

    sum_two_num=lambda num1,num2:num1+num2

    print("Sum of {0} and {1} is: {2}" .format(num1,num2,sum_two_num(num1,num2)))



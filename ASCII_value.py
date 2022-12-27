#1 print ASCII value 

a='A'
print('ASCII value of ',a,'is',ord(a))

#2 Print ASCII value of each characters in a string
text=(input('Enter the string:'))

txtlen=len(text)

for char in text:
    ascii=ord(char)

    print(char,'\t',ascii)
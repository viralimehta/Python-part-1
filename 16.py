'''Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.'''


a=17
b=int(input("input the integer:"))
if b>a:
    c=b-a
    print(2*c)
else:
    print(a-b)
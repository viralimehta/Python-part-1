'''Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.'''


def num(a,b,c):
    if(a == b == c):
        print(3*(a+b+c))
    else:
        print(a+b+c)


num(3,3,2)
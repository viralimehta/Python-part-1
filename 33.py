'''Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.'''


def num(a,b,c):
 if a==b or b==c or a==c:
    sum=0
 else:
    sum=a+b+c
 return sum

print(num(1,2,3))
print(num(2,2,1))
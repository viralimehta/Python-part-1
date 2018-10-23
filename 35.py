'''Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.'''

def values(a,b):
    sum=a+b
    dif=a-b
    if a==b or sum==5 or dif==5:
        return True
    else:
        return False
print(values(10,5))
print(values(5,5))
print(values(15,5))
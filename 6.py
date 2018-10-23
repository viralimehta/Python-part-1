'''Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.'''


a= input("Input some comma seprated numbers : ")
list = a.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
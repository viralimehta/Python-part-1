''' Write a Python program to get the size of an object in bytes.'''


import sys

str2 = "four"
str3 = "three"

print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")


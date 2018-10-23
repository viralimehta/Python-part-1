'''Write a Python program to determine if variable is defined or not.'''



try:
  x 
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
try:
  y=2
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")

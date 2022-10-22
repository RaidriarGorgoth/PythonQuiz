# addition
#subtraction
# mul
#divmod

import math


def addition(a, b):
    # RETURN THE ADDITION OF a and b


def subtraction(a, b):
    #RETURN THE SUBTRACTION OF a and b


def multiplication(a, b):
    #RETURN THE MULTIPLICATION OF a and b 


def division(a, b):
    #RETURN THE DIVISION OF a and b 


print("Options are:")
print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")

option = int(input("Enter your option"))


a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
result =0

if (option == 1):
  #CALL addition(a,b) and store in result variable
    print(result)
elif (option == 2):
  #CALL subtraction(a,b) and store in result variable
    print(result)
elif (option == 3):
  #CALL multiplication(a,b) and store in result variable
    print(result)
elif (option == 4):
  #CALL division(a,b) and store in result variable
    print(result)
else:
    print("wrong input")
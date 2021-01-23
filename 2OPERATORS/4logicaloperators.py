

# Logical operators: and or not are called logical operators.
# it can be applied to boolean and non boolean types, but the way they coperate are different.

#******************************************************************************************
#Logical Operators for Boolean Types
#******************************************************************************************

# logical and operators returns true only if both are true.
# print(True  and True)
# print(True  and False)
# print(False and True)
# print(False and False)

# Output ::  for the above scenario.

# True
# False
# False
# False

# Logical OR operator behaves opposite to the and, if any one of the operator is true then it returns true.
# print(True  or True)
# print(True  or False)
# print(False or True)
# print(False or False)

# Outpu::
# True
# True
# True
# False

# Not operator behaves the opposite to the return value.

# print(not(True  and True))
# print(not(True  and False))
# print(not(False and True))
# print(not(False and False))
# Output::  
# False
# True
# True
# True

# print(not(True  or True))
# print(not(True  or False))
# print(not(False or True))
# print(not(False or False))
# Output::
# False
# False
# False
# True

# Program to Accept the USername and Password check whether are they matching or not.

# username1="shyam"
# password1="beauty"

# username = input("Enter username")
# password= input("Enter password")

# if username==username1 and password==password1 :
#     print("Access Granted")
# else :
#     print("Unauthorized Access")



#******************************************************************************************
#                       Logical Operators for Non Boolean Types (and operator)
#******************************************************************************************

#Note//////////////////////////////////////////////////////////////////////////////////////
#                       0 means False, Non-Zero means True
#              Empty String , List, Set, Dict , Tuple are considered to False
# Let's consider following i.e applicability of logical operator for  non boolean operands.
# if the result of First operand evaluates to nonzero or True then the result is second operand.
# if resultant of First operand evaluates to zero or false, then the result is first operand.
# Here the resultant value will not be True / False but it will be either operand1 or operand2 only.
#Note//////////////////////////////////////////////////////////////////////////////////////

# print(1 and 10) 
# Output:: 10

# print(0 and 10)
# Here in this case the first expression ie 0 

# print("shyam" and "shyre")
# Output:: shyre
# print(False and "shyre")
# Output:: false
# print(0 and "20")
# print("" and "shyam")
# Output:empty
# print({} and 10)
# Output:{}
#boolean so its false 

# print(1 and 10)
# Output:: 10

# print(1 and 1)
# Output :: 1
# print(1 and 0)
# Output:: 0
# print(0 and 1)
# Output::0
# print(0 and 0)
# Output:0
# print(0 and False)
# Output::0
# print(0 and 0.0)
# Output::0



#******************************************************************************************
#                       Logical Operators for Non Boolean Types      (or) operator
#******************************************************************************************

#Note//////////////////////////////////////////////////////////////////////////////////////
#                       0 means False, Non-Zero means True
#              Empty String , List, Set, Dict , Tuple are considered to False
# Let's consider following i.e applicability of logical operator for  non boolean operands.
# if the result of First operand evaluates to nonzero or True then the result is first operand.
# if resultant of First operand evaluates to zero or false, then the result is second operand.
# Here the resultant value will not be True / False but it will be either operand1 or operand2 only.
#Note//////////////////////////////////////////////////////////////////////////////////////

# print(10 or 2)
# Output ::10
# print("shyam" or "apple")
# Output :: shyam
# print([] or 1)
# Output::1
# print(10 or [])
#Output::10
# print(1 or 3)
#output::1


#******************************************************************************************
#                       Not Operator for Non Boolean Types      
# Remember this doesnt result the operands but results true / false only.
#******************************************************************************************

print(not(1))
#Output:: False
print(not("shyam"))
#Output:: False
print(not(0))
#Output:: True
print(not(False))
#Output:: True
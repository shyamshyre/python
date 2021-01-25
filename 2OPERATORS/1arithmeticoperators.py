# Following are th operators in python.
# 1) Arithmetic operators ( + - * / % //(Floor Division) **(Exponential/Repeat))
# 2) Relational operators or Comparison operators
# 3) Logical operators    (and or not )
# 4) Equality operator    (== != is)
# 5) Assignment operators () 
# 6) Bitwise operators    (& ! ^ ~ << >>) (AND OR XOR COMPLEMENT LEFT SHIFT RIGHT SHIFT) 
# 7) Shift operators      ()
# 8) Terinary operators
# 9) Special operators
#     8.1) Identity operators
#     8.2) Membership operators
# 10) Operators precedence
# 11) Mathematical fucntions using Math Modulo 



# Arithmetic Operators.
# a=10
# b=2

# print(a+b)
# print(a-b)
# print(a*b)


# print(a/b) 
#Note//////////////////////////////////////////////////////////////
#      -5.0 In python always division return's floating point value
#Note//////////////////////////////////////////////////////////////

# print(a%b)

# a=10
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b) 
# Output:: is floor(3.333) ->3

# # Floor division operator returns both integer and float value.
# Conditions
# 1) if both the operands are integer it returns integer value.
# 2) if both the operands are float it returns integer value.
# 3) if either of the operands are float then it returns float value.
# ** By default the division operator reaturns floating value.
 

# a=10
# b=2.0
# print(a/b)
# print(a//b)
# #Output (5,5.0)
# print(10/2)
# # Output:: 5.0

# String multiplication or repeatition operator.
# print("shyam"*3)
# print("3*shyam")
# Ouput:: shyamshyamshyam


#Exponential Operators
#This is simply the power/ Exponential operator.
#print(2**3) =>8

#+ operator 
# print(10+20)

# # This acts as a concatenation operator.
# print("Shyam"+"Shyre")

# This resuts error in pythonic
# Note://Only + operator is used between two interger or two string operands only//
# print("shyam" +10)
# Output:: TypeError: can only concatenate str (not "int") to str

# print('Shyam'*'Shyre')
# Output: // Error as its not int.

# print(3*'shyam'*3)
# This is valid 
# Output::shyamshyamshyamshyamshyamshyamshyamshyamshyam

# When you are using * operator one operand should be int and other should be int
# When you are using * operator one operand should be int and other should be String

# concatenation
# print('shyam'*int('3'))


# Division by Zero , We get Zero Division Error
# print(1/0)
# ZeroDivisionError: division by zero
# print(1//0)
# ZeroDivisionError: division by zero
# print(1%0)
# ZeroDivisionError: division by zero

#boolean
# print('shyam'*True)
# True means 1
# Output::shyam
# print('shyam'*False)
# False means 0
# Output::

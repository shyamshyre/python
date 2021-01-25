# ~a  => Unary Operator
# a+b => Binary Operators

# a=100
# b=20

# Java sysntax notation of ternary operator
# c=(a>b) ? True : False

# Python Syntax Notation for ternary operator
#***********************************************
# first value if (conition) else (second value )
#***********************************************

# c=30 if(a>b) else 40 
# 100 greater than 20 condition is true so the result is first value i.e 30
# print(c)

# Program: Write a program 2 read int values from keyboard and print minimum value

# num1   = int(input("Enter number 1"))
# num2   = int(input("Enter number 2"))
# result = num1 if( num1 < num2) else  num2
# print("the minimum number is ", result)


# Concept 2: Nested Ternary Operators

# Write a program tp print minimum of 3 Numbers

# num1 = int(input("Enter number1"))
# num2 = int(input("Enter number2"))
# num3 = int(input("Enter number3"))


# result= num1 if(num1<num2 and num1<num3) else num2 if (num2 < num3) else num3

# In the first nested we are checking num1 is less than num2 or num3 
# if Condition1 fails then result is either num2 or num3 
# we are checking if num2 < num3 if result is true then print num2 or num3
#print(result)
# Maximum number
# result= num1 if(num1>num2 and num1>num3) else num2 if (num2 > num3) else num3
#print(result)


# Write a program tp print equal or max minimum of 2 Numbers

# a   = int(input("Enter number 1"))
# b   = int(input("Enter number 2"))
# result = "equal"if(a==b) else "smaller" if(a<b) else "bigger"      
# print(result)
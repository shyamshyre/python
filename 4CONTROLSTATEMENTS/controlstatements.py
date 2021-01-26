# All the Flow control statements are selected into 3 categories.
# 1) Selection Statements
# if
# if else
# if elif else
# if elif 

# 2) Itterative Statements.
# for 
# while

# 3) Transfer Statements
# break
# continue

# Keywords : pass & del

# There is no switch statement in python
# There is no dowhile statement in python
# There is no goto statement in python

# Condition1 if
# if statement should be followed by indentation

#  if condition :
#      statement1 
#      statement2
#      statement3
#      statement4
#   statement5
# All the above statements(1-4) are considered to be under the if block.
# The statement5 is not part of the block as it has  come out of the indentation.
# if we want to break the condition then again change the indentation

# a= input("Enter number 1 : ")
# b= input("Enter number 2 : ")
# if a<b:
#     print("Hello World")
#     print("Welcome to Python Revision")
# print("Welcome to Python Revision")

# Output:
# Enter number 1 : 1
# Enter number 2 : 2
# Hello World
# Welcome to Python Revision
# Welcome to Python Revision

# Enter number 1 : 30
# Enter number 2 : 10
# Welcome to Python Revision

# if a<b:
# print("This is hell")
# the above statement should be provided after indent which violates sysntax so results indentation error
# Output:: IndentationError: expected an indented block

# 2) Condition2 if else:
# Syntax:: if (condition ):
#             statement1
#             statement1X
#         else: 
#             tatement1
#             statement1X


# name=input("Enter name:: ")
# if(name =="shyam"):
#     print("Welcome to Python tutorials")
# else:
#     print("Sorry Unauthorized Access")
# print("Please visit again")

# Output::
# Enter name:: shyam
# Welcome to Python tutorials
# Please visit again

# Enter name:: ram
# Sorry Unauthorized Access
# Please visit again

# Condition 3 elif

# if condition  :
#     statement1
# elif condition: 
#     statement2
# elif condition:
#     statement3
# else:
#     default action

# team = input("Enter fav IPL Team")
# if(team =="CSK"):
#     print("Dhoni the King")
# elif(team=="RCB"):
#     print("Under the Ferrocious King")
# elif(team=="MBI"):
#     print("Mumbai Indians the Champions")
# elif(team=="SRH"):
#     print("SRH the weak batting team")
# else:
#     print("Sorry no such IPL team exists")

# Output::
# Enter fav IPL TeamMBI
# Mumbai Indians the Champions

# Enter fav IPL TeamCSK
# Dhoni the King

# Enter fav IPL TeamDBI
# Sorry no such IPL team exists




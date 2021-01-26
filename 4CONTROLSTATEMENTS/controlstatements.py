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

# Note:: in the above statemnt else: is not mandatory, its optional
# else acts as a default statement.

# Following are the 4 ways we can use the if statement
# Approach1

# if(condition)

# Approach2

# if(conditon) :
# else:

# Approach3
# # if (condition):
#  elif:

# Approach4

# if(conditon) :
# elif(conditon) :
# else(conditon) :

# Wap to print biggest of 2 numbers
# a= int(input("Enter number 1 : "))
# b= int(input("Enter number 2 : "))
# if(a>b):
#     print("A is bigger than B" ,a)
# else:
#     print("B is bigger than A" ,b)

# Wap to print biggest of 3 numbers
# a= int(input("Enter number a : "))
# b= int(input("Enter number b : "))
# c= int(input("Enter number c : "))
# if(a>b and a>c):
#     print("{} is bigger than {},{}".format(a,b,c))
# elif(b>c):
#     print("{} is bigger than {},{}".format(b,a,c))
# else:
#     print("{} is greater than {},{}".format(c,a,b))

# Wap to check whether the number is between 1 and 100 or not.
# a= int(input("Enter number a : "))
# if(a>=1 and a<=100):
#     print("Given input {} is between 1 and 100".format(a))
# else:
#     print("Sorry Enter the value between 1 and 100")

# Enter number a : 1
# Given input 1 is between 1 and 100

# Wap to print single digit number from keyboard and pring the number in words.
# no= int(input("Enter number : "))
# if(no==1):
#     print("ONE")
# elif(no==2):
#     print("TWO")
# elif(no==3):
#     print("THREE")
# elif(no==4):
#     print("FOUR")
# elif(no==5):
#     print("FIVE")
# elif(no==6):
#     print("SIX")
# elif(no==7):
#     print("SEVEN")
# elif(no==8):
#     print("EIGHT")
# elif(no==9):
#     print("NINE")
# elif(no==10):
#     print("TEN")
# else:
#     print("SORRY ENTER THE VALUE BETWEEN 1 AND 10 Only")

# Same Requirement using List
# no= int(input("Enter number : "))
# wordslist=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE,TEN']
# print(wordslist[no])

# Output:: Enter number : 4
# FOUR


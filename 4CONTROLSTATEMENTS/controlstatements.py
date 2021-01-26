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

# WAP to print the number to words (0-100)
# no= int(input("Enter number : "))
# oneslist=['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
# tenslist=['TEN','TWENTY','THIRTY','FORTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']
# tensidx=no//10
# onesidx=no-tensidx*10
#     or
#  onesidx = no%10
# if(no>10):
#     print(tenslist[tensidx-1]+" " +oneslist[onesidx])
# elif(no<10):
#     print(oneslist[onesidx])
# else:
#     print("Sorry Number Doesnt Exist in this range")

#****************************************************************
#               Itterative Statements
#****************************************************************


# for loop can be applied for 
# 1) String 
# 2) List 
# 3) Tuple
# 4) Dict
# 5) FrozenSet
# 6) Range etc..
# str= "India is my country"
# for c in str:
#     print(c)

# Index :: Printing index.
# str= input("Enter string input")
# idx=0
# for s in str:
#     print("the character present at {} index is {}".format(idx,s))
#     idx+=1 #(no increment idx++)

# Output::
# nter string inputindia
# the character present at 0 index is i
# the character present at 1 index is n
# the character present at 2 index is d
# the character present at 3 index is i
# the character present at 4 index is a

# Range data type:

# range(n) o to n-1
# range(min,max) min to max-1
# range(min,max,increment/decreemnt)

# for i in range(5):
#     print("Hello World")
# Output::
# Hello World
# Hello World
# Hello World
# Hello World
# Hello World

# Wap to print first 10 numbers
# for i in range(1,11):
#     print("Number",i)

# # Wap to print  odd numbers between 10
# for i in range(1,11,2):
#     print("Number",i)
# Ouput:: 
# Number 1
# Number 3
# Number 5
# Number 7
# Number 9

# # Wap to print  even numbers between 20
# for i in range(21):
#     if(i%2==0):
#         print(i)
# Output::
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# Wap to print odd numbers between 1 and 20
# for i in range(1,20):
#     if(i%2!=0):
#         print(i)
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19

# Wap to print numbers in desceding order 1-20

# for i in range(10,0,-1):
#     print(i)
# Output::
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# Wap to print even numbers in desceding order 1-20
# for i in range(20,1,-2):
#     print(i)

# Output::
# 20
# 18
# 16
# 14
# 12
# 10
# 8
# 6
# 4
# 2

# WAP to print the sum of given numbers in the given list
# l1=[10,20,30,40,50]
# for i in range(len(l1)):
#     print(l1[i])

# Output ::
# 10
# 20
# 30
# 40
# 50

# sum=0
# l1=[10,20,30,40,50]
# for i in range(len(l1)):
#     sum+=l1[i]
# print(sum)

# Output::
# 150


# list =  eval(input("Enter the numbers"))
# eval: converts the string to the type of input format that we are passing.
# Example [10,20,30]
# for i in list:
#     print(i)
# Enter the numbers[10,20,30]
# 10
# 20
# 30


# WAP to print to accept the input in dynamic list format and print their sum.
# sum=0
# l= eval(input("Enter the input in list format"))
# for i in range(len(l)):
#     sum+=l[i]
# print("The total sum is",sum)

# Enter the input in list format[10,20,30,40]
# The total sum is 100

# ****************Note:****************************
# For loop Syntax:
# for each x in <<sequence>>:
#     execute<<body>>
# For loop is based on the sequence
# ****************Note:*****************************

# while loop is based on the condition
# while condition:
#     execute<<body>>
# The loop exits only when the condition fails
# if you want to execute statements based on the condition then 
# use while loop.

# while range(0,10):
#     print("Welcome to Pyhton")
# Note:: if using range then it turns to be printing continously as it always turns true

# i=0
# while (i<10):
#     i+=1
#     print("Welcome to Pyhton")
# Output::
# Welcome to Pyhton
# Welcome to Pyhton
# Welcome to Pyhton
# Welcome to Pyhton
# Welcome to Pyhton
# Welcome to Pyhton
# Welcome to Pyhton
# Welcome to Pyhton
# Welcome to Pyhton
# Welcome to Pyhton

# WAP to print 1-20 numbers that are diivsible by3
# i=1
# while(i<=20):
#     if(i%3==0):
#         print(i)
#     i+=1

# Output::
# 3
# 6
# 9
# 12
# 15
# 18

# WAP to print sum of n numbers using keyboard
# i=0
# no = int(input("Enter the number of your choice"))
# sum=0
# while(i<=no):
#     sum+=i
#     i+=1
# print("The final sum value is ", sum)

# Wap to print country name till it takes as india
# name=""
# while(name!="india"):
#     name= input("Enter your favourite country name")
# print("Thank Tou, I too love India")

#Output
# Enter your favourite country nameusa
# Enter your favourite country nameamer
# Enter your favourite country namenigeria
# Enter your favourite country nameruss
# Enter your favourite country namechina
# Enter your favourite country nameindia
# Thank Tou, I too love India

#************************************************************
#************** INFINITE LOOP**************************
#************************************************************

# i=1
# while True:
#         print("No",i)
#         i=i+1
#         if(i>100):
#             break

# Printing 100 numbers using infinite loop


#************************************************************
#********************** NESTED LOOPS*************************
#************************************************************


# for i in range(3):
#     for j in range(2):
#         print("i Value {} j Value{}".format(i,j))

# output::
# i Value 0 j Value0
# i Value 0 j Value1
# i Value 1 j Value0
# i Value 1 j Value1
# i Value 2 j Value0
# i Value 2 j Value1


# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print()
        # print(i,j)
        # if(j==i):
        #     print(i,j)

# Output::

# *
# **
# ***
# ****
# *****







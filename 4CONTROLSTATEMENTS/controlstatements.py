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

#  name=input("Enter name:: ")
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

#  team = input("Enter fav IPL Team")
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

#  sum=0
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


#  for i in range(3):
#     for j in range(2):
#         print("i Value {} j Value{}".format(i,j))

# output::
# i Value 0 j Value0
# i Value 0 j Value1
# i Value 1 j Value0
# i Value 1 j Value1
# i Value 2 j Value0
# i Value 2 j Value1


#  for i in range(6):
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


# no= int(input("Enter the input number"))
# for j in range(2):
#     for i in range(no):
#             if(i!=no):
#                 print(" "*no+"* "*(i))
#                 else:
#                 print(" "*i+"* "*(no-i))


                

                # Break Statements
# Break statements are used to break execution of the loop.
# Once the break is executed immediately the loop is terminated
# Break is only used in itterative execution
# for i in range(0,10):
#         print("world is great")
#         if(i==3):
#                 break    
# print("Loop terminated")
# Ouput::
# world is great
# world is great
# world is great
# world is great
# Loop terminated

#  score=[10,20,30,100,110]
# for i in score:
#         print(i)
#         if (i>=100):
#                 print("Centurion and time to declare")
#                 break
# print("OOPs Missed 150")

# x=10
# if(x>30):
#         print("Working")
# break
# print("Hello World")
#     ^
# SyntaxError: 'break' outside loop
# Because should be used only under for,while loop , the same can be executed under loop.
# counter=0
# while(True):
#         counter+=1
#         if(counter>5):
#                 break
#         else:
#                 print(counter)
# Output::
# 1
# 2
# 3
# 4
# 5
# The above example is valid

#********************************* Continue Statements*******************
# Continue statement is used to skip the current itteration in the loop and 
# continue the next itteration.

# for i in range(5):
#         if(i==3):
#                 continue
#         print(i)

# Output::0 3 is skipped
# 1
# 2
# 4

# for i in range(10):
#     if(i%2==0):
#      continue
#     print(i)
# Output:
# 1
# 3
# 5
# 7
# 9

# Divide 100 by all the numbers inside the list 
# Anything by 0 will result zero division error so removing 0
# l=[10,20,0,30,40,0,50]
# result=0
# for i in range(len(l)):
#         if l[i]==0:
#          continue
#         else:
#                 result=100/l[i]
#                 print("Reuslt is{:.2f}".format(result))


# Note::****************************************************************
# Break and continue should be used with in the loop only.
#***********************************************************************

# for i in range(3):
#         for j in range(3):
#                 if i==j:
#                         break
#                 print(i,j)
# Output:
# 1 0
# 2 0
# 2 1


# for i in range(3):
#         for j in range(3):
#                 if i==j:
#                         continue
#                 print(i,j)

# Output::
# 0 1
# 0 2
# 1 0
# 1 2
# 2 0
# 2 1


#********************else with sequences(loops)*********************
# else can be used in conjuction with sequences(for/while) and even
# with try,# except,& finally
#*******************************************************************
# Note:: if the loop statement executed without any break statenment,
# then the else part is going to be executed. if not else block is not 
# going to be executed.

# for i in range(3):
#         if(i==2):
#                 continue
#         print(i)
# else:
#  print("Sorry its out of range")

#  Output::
# 0
# 1
# 2
# Sorry its out of range
# Since the loop got executed successfully so is the reason the else block got printed.

# for i in range(3):
#         if(i==2):
#                 break
#         print(i)
# else:
#  print("Sorry its out of range")

# Output::
# 0
# 1

# Wap to process all the elements value > 0 if its 0 then skip
# the processing and continue the rest.
# l=[10,20,0,30,40,50,0,60]
# for i in range(len(l)):
#         if(l[i]>0):
#                 print("{} is processing".format(l[i]))
#         else:
#          continue
# else:
#         print("All the elements successfully Processed Thank you")

# Output::
# 10 is processing
# 20 is processing
# 30 is processing
# 40 is processing
# 50 is processing
# 60 is processing
# All the elements successfully Processed Thank you

# When to use for loop and while loop
# For Loop: As long as we are processing sequnces.
# While Loop: As long as we are processing conditional based Itterative Statements.

# How to exit from loop?
# break

# how to skip the current itteration and continue the itteration
# continue

# else part can be used in for/while if there is no break statement being executed inside 
# the loop.

 
# pass : it acts as empty body or place holder for some implementation.
# Wherever we want empty body then we need to go for pass

# def f1():
# Ouput::SyntaxError: unexpected EOF while parsing

# def f1():
#         pass

# Output:: Successfully Execution Empty printe (but same is not printed)

# class A:
#         class B:
#                 class C:

# Output:: SyntaxError: unexpected EOF while parsing


# class A:
#         pass
#         class B:
#                 pass
#                 class C:
#                         pass

# Output:: Successfully Execution Empty printe (but same is not printed)

# x=9
# if x>10:
#         print("x is greater than 10")
# else:
#         pass
# x is greater than 10
# Output :: Empty in else condition
# Today we dont know what to write , but tomorrow we can change any message.
# AS already place holder exists so no issue or huge modification.


# 1. pass statement acts as empty statement
# 2. it acts as a place holder to implement the future code.
# 3. it can be used to define minimal classes and functions.
# 4. to define the abstract methods, pass statement is the best choice.


# Minimal Class Example
# class A:
#         pass
# ***********************

#  Minimal function Example
# def f1(): pass


#*********** Astract Method Example*******************
# from abc import ABC, abstractmethod


# class Loan(ABC):
#         @abstractmethod
#         def getInterestRate(self):
#                 pass
# class CarLoan(Loan):
#         def getInterestRate(self):
#                 return 12
# class HomeLoan(Loan):
#         def getInterestRate(self):
#                 return 8

#  cl = CarLoan()
# print(cl.getInterestRate())
# hl = HomeLoan()
# print(hl.getInterestRate())

#*************************************************************************************
#***************************************del Statement********************************
#*************************************************************************************
# del is used to delete reference variables from the memory.
# once the refernce variable are deleted from the memory, they are eligible for garbage collection



# x= 100
# print(x)
# del x
# print(x)
# NameError: name 'x' is not defined

#  str1= "We are indians"
# str2=str1
# str3=str2

# in the baove example stri,str2,str3 are reference variables that are pointing to object "We are indians"
# if we are deleting the str1 then still str2,str3 are pointing to same object so we can access str2,str3
# del str1
# Output: NameError: name 'str1' is not defined
# print(str1)
# print(str2)
# print(str3)
# Output::
# We are indians
# We are indians
# del str1, str2, str3
# print(str1,str2,str3)
# O/p::NameError: name 'str1' is not defined

# 2. del VS Immutable Objects

# s="Test String"
# del s
# print(s)
# Output:NameError: name 's' is not defined
# del s[0], We cannot delete T from the memory as its immutable object.
# TypeError: 'str' object doesn't support item deletion
# del cannot delete immutable objects but it can delete reference variables pointing to immutable objects

# 3.del vs None
# x= 10
# x= None
# print(x)
# Here the x is pointing to 10 object initially, later we have assigned to None
# so the 10 doesnt exist, eligible for gc but still we can access x as its mapped to None.


# Summary:
# del is a keyword in pyhtonl
# del is used to delete refernce variables 
# del cannot delete the content inside the immutable objects, but it can delete the rference variables.
# When we are asigning none to reference variables it represents nothing, 
# Ex: reassiging a variable None to existing variable.
#     then the previous object eleigible for gc.



# # Wap to check whether the number is prime or not.

# i sprime=True
# no = int(input("Enter the no to check whether its prime or not ?"))
# i=1
# if no <=1 :
#         print("Values should be greater than 1")
# else :
#         for i in range(1,no-1):
#                 print(i)
#                 if (no%i==0):
#                         # print("Given number {} is composite".format(no))
#                         isprime=False
#                         break
                        
#         if(isprime == False):
#                 print(isprime)
#                 print("Given number {} is not prime".format(no))
#         else:
#                 print(isprime)
#                 print("Given number {} is prime".format(no))



# Wap to print all the list of prime numbers between the number provided.

prime=True
no = int(input("Enter the no to check whether its prime or not ?"))
i,j=0,0
if no <=1 :
        print("Values should be greater than 1")
else :
        for i in range(1,no-1): 
                i+=1
                for j in range(1,i-1):
                        j+=1
                        #print("i",i ,"j",j)
                        if(i%j==0):
                                prime=False
                                print("Composite Number  {}".format(i))
                                break
                                
                        elif(prime == False and i!=2):
                                print("Prime Number  {}".format(i))

# Reading Data through command line arguments.

# 1) Using the input() method.
# num1 =  int(input("Enter the number1"))
# num2 =  int(input("Enter the number2"))
# print(type(num1))
# print(type(num2))
# print(num1+num2)

# # 2) Reading Multiple command line arguments.
# a,b= [int(x) for x in  input("Enter multiple arguments").split()]
# print(a,b)
# Input :: 10 20 30 
# Output:: ValueError: too many values to unpack (expected 2)
# Input :: 10 20
# Output:: 10 20

# Reading the arguments from the keyboard using arguments
# from sys import argv
# print(type(argv))
# Output: <class 'list'>

# from sys import argv
# print(len(argv))
# for i in argv:
#     print(i)
# Output :: inputoutput.py a b c  
# First argument is the file name


# from sys import argv
# print(type(argv))

# from sys import argv
# print("The number of Command line Arguments : " ,len(argv))
# print("The list of Command Line Arguments : ", argv)
# print("Command Line Arguments One by One")
# for i in argv:
#     print(i)

# from sys import argv
# sum = 0
# counter = 0
# args = argv[1:]
# for i in args :
#     sum = int(i)+sum
#     counter += 1
#     if (len(args) == counter):
#       print(int(sum))
# Input :: 10 20 30 
# Ouput :: 60


# Eval function is used to convert the string content to coerresponding data types.
# print(eval("10"))
# print(eval("10+20+30"))
# print(eval("10+20+30/4"))
   


# from sys import argv
# args = argv[1:len(argv)]
# for i in args :
#     print(i)
#  Output: 10
# 20
# 30  

# sum = sum+int(i)
# print(sum)

# For Loop if u are capturing result in one variable then its a list
# result = [int(i) for i in input("Enter the params").split()]
# print(type(result))
# print(result)

# Output :: 
# Enter the params12 21
# <class 'list'>
# [12, 21]

# if we are not capturing result in single variable then its conversion data type but not list
# a,b = [int(i) for i in input("Enter the params").split()]
# print(type(a))
# print(a)

# Output : <class 'int'>
# Output : 12

# *************************************Remember***********************************
#                     eval() only takes enclosed string expression.
# ********************************************************************************
# a="10"
# b="20"
# print(eval(a+b))
# Ouput:1020 but not 30

# l= eval(input("Enter the input"))
# print(type(l))


# num1= eval(input("Enter the number 1"))
# num2= eval(input("Enter the number 2"))
# print(num1+num2)
# Output :: 30


# fixedlen=100
# print(100*"*")
# l=['Welcome','to','World', 'of','Programming']
# for i in l:
#     stringlen = len(i)   
#     startpos = int(fixedlen-stringlen)//2
#     endpos = 100 - startpos-stringlen
#     #print(startpos*'*'+i,sep=''+endpos*'*')
#     print(startpos*'*'+i+endpos*'*')
# print(100*"*")

# Output:
# ****************************************************************************************************
# **********************************************Welcome***********************************************
# *************************************************to*************************************************
# ***********************************************World************************************************
# *************************************************of*************************************************
# ********************************************Programming*********************************************
# ****************************************************************************************************


# Format 1:
# Displaying variable data using % notation.
# a,b ='Shyam',100
# print("%s got %i marks in Maths Exam" %(a,b))

# Format 2:
# Displaying variable/ identifiers data using {} notation.
# name='Shyam'
# marks=100
# you should use as the seperator to print the data using paranthesis.
# print("{0} got {1} marks in maths exams". format(name,marks))

# Format 3:
# # Displaying the variable data using sep keyword.
# a,b ='10','Shyam'
# print(a, b, sep=':')

# # Format 4:
# a='Shyam'
# list=[10,20,30,40]
# print("%s got following marks %s" %(a,list))



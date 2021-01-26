# Input and output Statements

# Input Statements
# 1) raw_input() vs input() 
# 2) python3 -input function.
# 3) Reading multiple values from a single line.
# 4) Command line Arguments
# # Ouput Statements
# 5) print() 
# 6) sep Attribute
# 7) end Attribute
# 8) printing formatted string.
# 9) Replacement operator {}

# raw_input() : The return type of this method is string only.

# Note::  # We need to perform type casting.
# x= print("Enter the input number")
# print(type(x)) 
# Ouput :: String
# y= int(x)

# input() :: This is intelligent fuction it  returns the value based on the input 
# provided by end user input
# Note:: There is no need to perform any type of casting
# Above both functions exists in python2 but not in python3

# Python 3:: 
# Whats the return types of input() ?
# Its string, this method is a as equivalent to raw_input() in Python2.0 so it returns
# string only.
# x= input("Enter input number")
# print(type(x))
# Ouptut:<class 'str'>
# We need to use explicity use type casting to convert to another data types.
# As string is most commonly used type so python team provided preference to string type.

# Wap to print sum of 2 numbers
# a = int(input("Enter a value : "))
# b = int(input ("Enter b value : "))
# print("Total Sum" , a+b)
# Output::
# Enter a value : 1
# Enter b value : 2
# Total Sum 3

# Printing in single line
# print("the Sum is",  int(input("Enter a value : ")) + int(input("Enter a value : ")))

# Output::
# Enter a value : 1
# Enter a value : 2
# the Sum is 3

#Command Line arguments
# Arguments passed through command line

# from sys import argv
# # Note :: argv is list type
# # print(type(argv))
# print("The length of argumnet",len(argv))

# Note:: the first argument is file name
#  inputoutput 1 2 3
# Output:: inputoutput.py
# total=0

# we should assign the argv to the new variable if trying to get the value from args it leads to error
# args= argv[1:]
# for i in args:
#     total+= int(i) 
#     print(total)
    

# Reading command line arguments with space.
# Lets suppose we are reading input with space Ex: (Mera Bharath) all this is one word.
# But as the space is the default delimeter , if we want to consider Mera Bharath as one word.
# Just enclose with docuble quotes "Mera Bharath".
# Now this is considered as the single word.


# Case1:
# from sys import argv
# slogan = argv[1]
# print(slogan)
# Output: Mera Bharath

# Case2
# from sys import argv
# total = argv[1] + argv[2]
# print(total)
# It acts as concatenation as the default command line arguments format is string.
# Input: inputoutput.py 1 2
# Ouput: 12


#Case3
# from sys import argv
# total = int(argv[1]) + int(argv[2])
# print(total)
#It acts as concatenation as the default command line arguments format is string.
# Input: inputoutput.py 1 2
# Ouput: 3

#Case4 (If accessing index greater than the arguments passed leads to indexerror)
# from sys import argv
# total = int(argv[1]) + int(argv[2])
# print(argv[3])
# Input: inputoutput.py 1 2
# IndexError: list index out of range



# *******************************************************************************
#                             OUTPUT STATEMENTS
# *******************************************************************************

# Form -1
# print () -> withnout any argument (this inserts new line character \n)
# print("Love")
# print() --> /n
# print("India")
# Output:
# Love

# India

# Form-2
# print("\tI \n Love \n India")
# We can include escape characters in the string.
#         I 
#  Love 
#  India
# print("India" + "is my country")
# Indiais my country
# print(10*"India") - > String repeatition operator
# IndiaIndiaIndiaIndiaIndiaIndiaIndiaIndiaIndiaIndia

# Form-3 printing string with multiple arguments
# This feasability is not in any  other languages.
# a,b,c=10,20,30
# print("Values are ",a,b,c)
# Ouptut:: Values are  10 20 30 (space exists betweeen 10,20 and 30)
# Observe the ouput space exist between the above output.

# Seperator (sep) Attribute
# if we want to format string as per our customized delimeter
# Default space is removed by :
# a,b,c=10,20,30
# print(a,b,c,sep=':')
# output 10:20:30
# print(a,b,c,sep='$')
# 10$20$30

# End (end) Attribute 
# Defualt end character is seperated by the | sysmbol default newline character 
# is replaced by custom character of our choice.
# print("I", end="|")
# print("Love",end="|")
# print("India")
# Output: I|Love|India

# print("I", end="***")
# print("Love",end="::")
# print("India")
# Output:I***Love::India



# Differnce between sep and end.
# sep is used in between the varaiables, where as end is used at the end of the line.

# WAP to demonstrate Using of both sep and end .
# a,b = "India","is"
# c= "my country"
# print(a,b,sep=":",end=":")
# print(c,sep=":")
# Output :: India:is:my country

# print("I"+"Love"+"India")
# print("I","Love","India")
# Output:: 
# ILoveIndia : No space when we use concatinaton.
# I Love India : Default spcae is the seperator



# # Note:: { } oeprator need to be used in combination with format.
# print("{mycoutry} is my country".format(mycoutry=country))


# Form 1:
# name="Shyam"
# topic="Python"

# print("Mr. {} is helping to teach {}".format(name,topic))
# Output:: Mr. Shyam is helping to teach Python
# Here the order of the attributes specified in the argument is important the elements 
# take them in the same format
# Note:: In this approachif the value are interchanged the output gets intechanged, as
#  we are notaware what is getting printed.


# Form 2:  Indexing Approach.
# Printing the values can be done by using index.
#print("Mr. {0} is helping to teach {1}".format(name,topic))
# ASsume after format its a tuple, now we can print values from the tupe using index.
# Output:: Mr. Shyam is helping to teach Python

# Form 3: Key Word Arguments Approach.
# name="Shyam"
# topic="Python"
# print("Mr. {isntructor} is helping to teach {subject}".format(isntructor=name,subject=topic))
# Here we are filling the replacement operator with variable name so that we are aware what is to be printed.

# WAP to print a=10,b=20,c=30,d=40
# a,b,c,d=10,20,30,40
# print("a={},b=20,c={},d={}".format(a,b,c,d))
# Without format operator if we want to print same.
# print('a=',a,'b=',b,'c=',c,'d=',d)


# print() with Formatted String
# %i -int()
# %d -int()
# %f -float()
# %s -String, any other collection objects i.e list,set.. etc
# Syantax: print("formattedstring",%(varablelist)) 

# country="India"
# print("%s is my country" %(country))

# marks=[100,100,90,90,89]
# name="Shyam"
# print("%s marks are %s" %(name,marks))
# Output:: Shyam marks are [100, 100, 90, 90, 89]

# dollarvalue = 73.878989898
# print("Today dollar value is {}".format(dollarvalue))
# print("Today dollar value is %f" %(dollarvalue))
# If i want do custom formatting like rouding to 2 digits.
# This can be done only with 2nd approach.
# Today dollar value is 73.878989898
# Today dollar value is 73.878990
# print("Today dollar value is %.2f" %(dollarvalue))
# Today dollar value is 73.88












#Reading multiple inputs from a single line.
# a,b= [int(i) for i in input("Enter the inputs").split(" ")]
# print(a)
# print(b)


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

#  templist=[]
# total = 0
# templist=([int(i)for i in input("Enter numbers").split()])
# for i in templist :
#     total+=i
#     if (i== len(templist)):
#      print("sum of value", total )


# bill =10.323232
# print("the final bill is %f" %bill)
# print(" the final formmated value {:.2f}".format(round(bill),2))
# print(" the value id {x}".format(x=100))

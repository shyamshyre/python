#Program 1
# Input:5
# Output: * * * * *
# no = int(input("Enter the input number"))
# for i in range(no):
#     print("*",end=' ')

# Input:5
# Output: * * * 
        # * * * 
        # * * * 


#Program 2
# no1 = int(input("Enter the number"))
# for i in range(no1):
#     for j in range(no1):
#            print("*",end=' ')
#     print()
# Output :: 
# * * * 
# * * * 
# * * * 

#Program 3
# no1=int(input("Enter the number"))
# for i in range(no1):
#     print("*"*no1)
# Output::***
#         ***
#         ***

#Program 4
# Expected Result: 
# 111
# 222
# 333

# no1=int(input("Enter the number"))
# idx=1
# for i in range(no1):
#     print(str(idx)*no1)
#     idx+=1
# Output::
# Enter the number4
# 1111
# 2222
# 3333
# 4444    

#Program 5
# Enter the input :4
# AAAA
# BBBB
# CCCC
# DDDD
# idx=0
# no = int(input("Enter the number"))
# for i in range(no):
#     print(chr(65+idx)*no)
#     idx+=1

# Enter the number3
# AAA
# BBB
# CCC


# Program 6
# *
# * *
# * * *
# idx=1
# no= int(input("Enter the input number"))
# for i in range(no):
#     print('*'*idx)
#     idx+=1

# Output::
# Enter the input number3
# *
# **
# ***


# Program 7
# Wap to print the table of your choice
# no = int(input("Enter the table of your choice"))
# idx=1
# value=0
# for i in range(11):   
#     value = no*idx
#     print(str(no)+"*"+str(idx)+"="+str(value))
#     idx+=1


# Program 8
# * * *
# * *
# * 
# idx=1
# no= int(input("Enter the input number"))
# for i in range(no):
#     print('*'*no) 
#     no-=1    

# Output:
# ***
# **
# *


# WAP to print pyramid
#     *
#    *  *
#   *  *  *  

# idx=1
# no= int(input("Enter the input number"))
# space=no
# for i in range(no):
#     print(" " * space,end="")
#     print('* '*(i+1)) 
#     idx+=1 
#     space-=1
# Output::1
# Enter the input number4
#     * 
#    * * 
#   * * * 
#  * * * *


# WAP to print invert pyramid
# no= int(input("Enter the input number"))
# for i in range(no):
#         print(" "*i+"* "*(no-i))

# Enter the input number3
# * * * 
#  * * 
#   * 

# WAP to print diamond 
no= int(input("Enter the input number"))
for i in range(2):
        for j in range(no):
                 print(" "*(no-j)+"* "*j) if(i==0) else print(" "*j+"* "*(no-j))
                 # Printing the same using ternary notation
# Output::
#    * 
#   * * 
#  * * * 
# * * * * 
#  * * * 
#   * * 
#    * 
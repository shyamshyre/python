# == and != are called Equality Operators

# To check the values are qual or not we use equality operators
# a=10
# b=20
# print(a==b)
# print(a!=b)
# Output::
# False
# True

# print(1==True)
# # Output:: True

# print(1==1.0)
# # Output:: True

# print("shyam"=="shyam")
# # Output:: True

# print(10 == "shyam")
# # Ouput is False
#Note//////////////////////////////////////////////////////////////
# In relational operators we cannot compare between string & numbers
# But here in equality operators we can compare and it returns false 

# print(10 == 20 == 30 ==40)
# Output:: False


# print(10 == 10 == 30 ==40)
# Output ::  False


# Difference between == & is operator
# if both the operands are representing / pointing to the same object then only it returns true.
# is operator compares address/ reference comparison 
# == compares the content where as is compares the address location.
# Ex : 
# a = 10
# b = a
# c = 10.0
# d = 1
# e = True
# print(id(a))
# print(id(b))
# print(a is b)
# print(a is c)
# print(a == c)
# print(d == e)
# print(d is e)
# Output :: 
# 4337757120
# 4337757120
# True
# False
# True
# True
# False
# print(2==3)
# False
# print(2 is 3)
# False
# l1=[10,20,30]
# l2=[10,20,30]
# print(id(l1))
# 140558442442432
# print(id(l2))
# 140558442441856
# print(l1 is l2) 
# False
# print(l1 == l2)
# True

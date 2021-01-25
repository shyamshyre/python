# There are 2 special operators
# 1) Idenity operator (IS ,IS NOT)
# 2) Membership operator

# IS :  if both the objects are refering to same memory location.
# IS NOT :  if both the objects are refering to different memory location.

# a=10
# b=10
# c=20
# print(a is b)
# print(a is c)
# l1=[10,20,30]
# l2=[10,20,30]
# print(l1 is l2)
# print(l1 is not l2)
# Output :: 
# True
# False
# False
# True


# 2) Membership Operator
 # IS This checks whether the value is in collection or not , Returns `TRUE if exists.
 # IS NOT This checks whether the value is not inside  collection or not, Returns TRUE if doesnt exists. 
 
#  s = "Welcome to world of python"
# print('z' in s)
# Ouptut : False

#  s = "Welcome to world of python"
# print('z' not in s)
# output : True

#  l=[10,20,40,50,60]
# print(30 in l)
# Outptut : False  
# l=[10,20,40,50,60]
# print(30 not in l)
# Outptut : True 
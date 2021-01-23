# Realtional /Comparison Operators.
# < <= > >=
# a = 10
# b = 20
# print(a<b)
# Output:: True
# print(a>b)
# Output:: False
# print(a<=b)
# Output:: True
# print(a>=b)
# Output:: False

# Even we can compare the string, because the string internally are converted to ASCII code.
# A-Z ascii code is less when compared to a-z
# unicode A  = 65
# unicode a  = 97

# To get the corresponding ordinal/unicode value.
# this returns the unicode value 
# print(ord('a'))
# Output:: 97
# print(chr(65))
# Output:: A

# a = 'apple'
# b = 'orange'
# it compares the first ascci character of the string ie 'a' and 'o'
# 'o' is greater when compared to 'a' so the output of a<b would be True.
# print(a<b) 
# print(a<=b)
# print(a>b)
# print(a>=b)

# Output::
# True
# True
# False
# False

# a = 'apple'
# b = 'apple'
# print(a<b)
# print(a<=b)
# print(a>b)
# print(a>=b)

# Output
# False
# True
# False
# True

# Relational operators can be even applicable for boolean
# print(True >False)
# print(True >=False)
# print(True <False)
# print(True <=False)
# Output
# True
# True
# False
# False

#Note//////////////////////////////////////////////////////////////
#print(10 < 'Shyam')
# Comparison operatorscan be only appied for string / numerical values
# but not for string & int.
# Output::
# TypeError: '<' not supported between instances of 'int' and 'str'


# a=10
# b=20
# if (a>b):
#     print("A is greater than B")
# else:
#     print("B is greater than A")

# Output::
# B is greater than A


# Relational Operators
# Chaining of operators
# print(10<20)
# print(10<20<30)
# print(10<20<30<40)
# print(10<20<30<40>50)
# Among the chain if any one results false , complete result is false.
# if any one of the condition is False , complete result is False
# output::
# True
# True
# True
# False

# print(10 == '10')
# Output:: False , As they are incompatible.





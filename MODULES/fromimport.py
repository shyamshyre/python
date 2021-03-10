# Instead of calling the module or alias we can call the other modules variables , functions by using from import

# Option1 : calling the selected information
# from mathmod import add,mul

# print(add(10,20))


#  Option2 : calling the all the variables and methods  from other module by using *
from mathmod import *
print(add(10,20))
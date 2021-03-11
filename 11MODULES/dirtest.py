# print(dir())
# As nothing is passed so we get the following information
# Output::['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

# ''' add() method accepts two params as the input and return the sum of two params'''
# def add(x,y):
#     return x+y

# print(__doc__)
# print(__file__)
# print(__name__)

# Return the filename with its absolute path

# import os
# print("File Name",__file__)
# print("Absolute Path",os.path.abspath(__file__))
# print("Directory Name",os.path.dirname(os.path.abspath(__file__)))

# ===========Example2======
# import mod1
# print("Calling Directly ")
# print("Calling from Direct Test")
# mod1.f1()

# Output::

# F1()
# F2()
# F3()
# Calling Directly 
# Calling from Direct Test
# F1()

# Calling all the methods in the mod1 and f1 from dirtest


# Question == ? How do we only call f1() from the dirtest
# Answer is : we need to verify the code whether its executed directly or indirectly


import mod1
print("Calling Directly ")
print("Calling from Direct Test")
mod1.f1()

# Output::
# Calling Directly 
# Calling from Direct Test
# F1()
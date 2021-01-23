# Following are the Bitwise operators in python.
# &  -> Bitwise AND operator.
# |  -> Bitwise OR operator.
# ^  -> Bitwuse XOR operator.
# ~  -> Bitwise Complement operator.
# << -> Bitwise Left Shift operator.
# >> -> Bitwise Right Shift operator.
# We can only apply Bitwise operators for int and boolean types only.
# if we are applying for any other data types then python returns TypeError.


# 1) Bitwise & operator
# print("shyam" & "shyam")
# TypeError: unsupported operand type(s) for &: 'str' and 'str'
# print(10.0 & 10)
# TypeError: unsupported operand type(s) for &: 'str' and 'str'
# print(bin(3))

#Binary Numbers.
#  
#  000
#  001
#  010
#  011
#  100
#  101
#  110
#  111
# 1000 

# print(8 & 8)
# 1000
# &
# 1000
# ----
# 1000 And operator: if both bits are 1 then only the result is 1 else 0
# ----

# print(5 & 6)
# Output::4
# 101
# 110
# ---
# 100 (4)
# ---

# 2) Bitwise | operator

# |  operator
# if atleast one bit is 1 then the result is 1

# print(5 | 6)
# Output:: 7
# 101
# 110
# ---
# 111 (7)
# ---
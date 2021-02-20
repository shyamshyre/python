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

# 2) Bitwise ^(XOR) operator
# if any of the bits are 0 and 1 then the result is 1
# if both bits are 0 then the result is 0
# if both bits are 1 then the result is 0

# 100
# 101
# ---
# 001 (Result is 1)
# ---

# AND(&)  OR(|)  XOR(^)
# 101     101    101
# 110     110    110
# ----    ----   ----
# 100 (4) 111(7) 011(3)
# ----    ----   ----    


# 4) Bitwise complement(~)tild operator
# print(~(4)) 
# Output:: -5

# Lets represent the same in 32 bit notation.
#4 - integer and positive number.
# 0000 0000 0000 0000 0000 0000 0000 0000 0100
# The first digit represent the MSB which is the sign bit.
# All the positive numbers denote 0
# All the negative numbers denote 1

# ~(4) Interchange 0's with1 and 1's with 0

#   (4) 
 
#  1111 1111 1111 1111 1111 1111 1111 1111 1011 (~4)
#  THE MSB is 1 (Left Most Bit)
#  if its negative the principal is 1's compliment +1 in memory.
#  if its positive (0) then they remain unchanged in memory.

#  1111 1111 1111 1111 1111 1111 1111 1111 1011 (~4)

#  1000 0000 0000 0000 0000 0000 0000 0000 0100 (1's Compliment)
#                                             1 (+)
# ----------------------------------------------
#  1000 0000 0000 0000 0000 0000 0000 0000 0101  (MSB1)  -> Negative 101(3)
# ----------------------------------------------
# Answer is -5
# -----------------------------------------------

# Odd Numbers
# print(~(-5))              print(~(-3))
# 1101 (-5)                 1011 
#  010 (1's Compliment)      100   
#    1 (+1)                    1
# 1011 Result                101
# 0100 ~(Result)(4)         0010  (2)

#print(~(-4))
#  1100 (-4)
#   011 (1's compliment)
#     1 +1
#---------
#   100 (2'Scompliment) 1+1 (will reuslt 0 and then its added as carry forward to next bit)  
#---------
#   011 ~(Final result) 3

#Even Number's
#print(bin(-6))
# print(~(-6))
# 1 110 (-6)
#   001 
#     1 (Final Result) 1+1 (will reuslt 0 and then its added as carry forward to next bit)  
#   010
# 0 101

# Bitwise Left Shift operator
# Shift the values by the operand of our choice.
# Ex: (10<<3) 10 Left Shit 2
# Step1: Representing in binary format.
# positive number so msb is 0..1010
# 0000 0000 0000 0000 0000 0000 0000 0000 1010
# Objective shifting 10 by 2 
# When we are shiftng it by 2 bits i.e the left most 2 bits are removed and two 0's are added at the end.
# 00 0000 0000 0000 0000 0000 0000 0000 101000
# print(10<<2)
# Output:: 40

# Bitwise Right Shift operator
# Shift the values by the operand of our choice.
# Ex: (10>>3) 10 Right Shit 2
# Step1: Representing in binary format.
# positive number so msb is 0..1010
# 0000 0000 0000 0000 0000 0000 0000 0000 1010
# Objective shifting 10 by 2 
# When we are shiftng it by 2 bits i.e the right most 2 bits are removed and the moved 2 bits i.e right most bits are replaced by MSB .
# Since the value is +ve right side 2 bits would be 0 and the left side shifted bits 10 would be vanished
# 000000 0000 0000 0000 0000 0000 0000 0000 10
# print(10>>2)
# Output::2

# Summary::
# Bitwise operators can only be applied for integer and boolean data  Types
# True is represented as 1 and False is represented as 0 and rest of the above principal remains same.
# its as simple as you are doing it for integer 0 and1
print(True<<2)
# Original  :: 00....01
# Left Shift:: xx....0100 (4)
# Output:: 4
print(True>>2)
# Original  :: 00....01
#              0000 ....00(0)
# Output:: 0
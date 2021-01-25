# Operators precedence
# Which operator executes first 

# () -> Paranthesis
# ** -> exponential
# ~- -> Bitwise complement & unary minus operator
# */%// => multiply, division,modulo, flor division
# +- => add, sub
# << >> =>left shift , right shift
# &  => Bitwise AND 
# ^  => Bitwise XOR 
# |  => Bitwise OR
# < ,<= , >,>= != == Relational operator
# = , == , += ,*= ,... Assignment operator
# is , isnot => Identity operator
# in , not in =>membership operator
# not => logical not
# and => logical and
# or  => logical or


# print(10+2*3)
# first mul then added
# Output::16

# print((10+2)*3)
# First parentheses then multiplication
# 12*3 = 36

# a= 30
# b= 20
# c= 10
# d=5

# print((a+b)*c/d)

# First priority () -> (30+20) =50
# Second priority () -> multiplication , division having same precedence , so need to go from left to Right
# 50*10 =500
# 500/5 =100.0 (always division returns floating value only)


# (a+b) * (c/d)
# 50 * 2.0 = 100.0

#(a+(b*c)/d)
#  b*c= 200
#  200/5 =40.0
#  30+40.0
#  70.0

# print(3/2*4+3+(10/5)**3-2)
#   3/2*4+3+2**3-2  
#   3/2*4+3+8-2
#   1.5*4+3+8-2
#   6.0+3+8-2
#   17.0-2 =15.0
# Ouput ::  15.0
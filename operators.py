"""Operators will perform operations on variables and values. 
Python uses operators for the following"""
#Arithmetic 
#Assignment 
#Comparison
#Logic
#Identity
#Membership
#Bitwise

#ARTHMETIC OPERATORS
#+(Addition), -(Substraction), *(Multiplication), /(Division), 
#%(Modulus aka remainder after division), **(Exponentiation), // (Floor division aka division with no remainders allowed)

#ASSIGNMENT OPRATORS
# =     x =  5 same as x = 5
# +=    x += 3 same as x = x+3
# -=    x -= 3 same as x = x-3
# *=    x *= 3 same as x = x*3
# /=    x /= 3 same as x = x/3
# %=    x %= 3 same as x = x%3
# //=   x //=3 same as x = x//3
# **=   x **=3 same as x = x**3
# &=    x &= 3 same as x = x&3
# |=    x |= 3 same as x = x|3
# ^=    x ^= 3 same as x = x^3
# >>=   x >>=3 same as x = x>>3
# <<=   x <<=3 same as x = x<<3

#COMPARISON OPERATORS

# ==(Equal), != (Not Equal), > (Greater than), < (Less than), >=(Greater than or Equal to)
# <=(Less than or Equal to)

#LOGICAL OPERATORS
"Used to combine conditional statements"
#and Returns true if both statements are True 
x>5 and x<10
#or  Returns true if one of the statements is true
x<5 or x>10
#not Reverse the result, False if result is true
not(x>5 and x<10)

IDENTITY OPERATORS
""" Used to compare if two variables are the same object with the same memory location"""
# "is"      Returns True if both variables are the same object (x is y)
# "is not"" Returns True if both variables are not the same object (x is not y)

MEMBERSHIP OPERATORS
""" Used to test if a sequence is presented in an object"""
# "in"   Returns True if a sequence with the specified value is present in the object 
# "not in" Returns True if a sequence with the specified value is not present in the object

BITWISE OPERATORS
""" Used to compare binary numbers"""
# &     it is an AND operator   sets each bit to 1 if both bits are 1
# |     it is an OR  operator   sets each bit to 1 if one of two bits is 1
# ^     it is a  XOR operator   sets each bit to 1 if only one of the bits is 1
# ~     it is a  NOT operator   Inverts all the bits
# << Zero fill left shift. it shifts left by pushing seros in from the right and let the leftmost bits fall off
# >> Signed right shift. Shift right by pushing copies of the leftmost bit in from the left and lets the rightmost bits fall off




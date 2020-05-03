
#Data Types

""" python has 14 built-in data types grouped in seven categories:

Text    type      str
Numeric type      int, float, complex
Sequence type     list,tuple, range
mapping type      dict
set type          set, frozenset
boolean type      bool
binary type       bytes, bytearray, memoryview
"""
#type() function to get the data type
x = 5
print(x)
print(type(x))

""" Python sets the data type automatically when you assign a value to a variable.
Note how the different types are presented, (). [], {} or functions followed by ()"""

x = "john"                       # python sets the str        data type TEXT     DATA

x = 5                            # python sets the int        data type NUMERIC  DATA
x = 5.2                          # python sets the float      data type NUMERIC  DATA
x = 1j                           # python sets the complex    data type NUMERIC  DATA

x = [1,5,7]                      # python sets the list       data type SEQUENCE DATA
x = (1,5,7)                      # python sets the tuple      data type SEQUENCE DATA
x = range(5)                     # python sets the range      data type SEQUENCE DATA

x = {1,5,7}                      # python sets the set        data type SET      DATA
x = frozenset({1,5,7})           # python sets the frozenset  data type SET      DATA 

x = {"Name" : "john", "Age": 18} # python sets the dict       data type MAPPING  DATA

x = True                         # python sets the bool       data type BOOLEAN  DATA

x = b"a_certain_String"          # python sets the bytes      data type BINARY   DATA
x = bytearray(5)                 # python sets the bytearray  data type BINARY   DATA
x = memoryview(bytes(5))         # python sets the memoryview data type BINARY   DATA

""" Sometimes you will have to specify the datatype in your coding.
Here are python constructor functions for wach data type.
note all functinos are followed by ()
and all the previous type syntax as [], and {} become parathesiss too"""

x = str("John")                  # specifies the value of x as a string type

x = int(5)                       # specifies the value of x as an integer type
x = float(5.2)                   # specifies the value of x as a float type
x = complex(5j)                  # specifies the value of x as a complex number type

x = list((1,5,7))                # specifies the value of x as a list type *note the [] became ()
x = tuple((1,5,7))               # specifies the value of x as a tuple type 
x = range(5)                     # specifies the value of x as a range type 

x = set((1,5,7))                 # specifies the value of x as a set type * note the [] became ()
x = frozenset((1,5,7))           # specifies the value of x as a frozen set type 

x = dict(name = "John", age = 18)# specifies the value of x as a dictionary type *much simpler

x = bool(5)                      # specifies the value of x as a boolean type 

x = bytes(5)                     # specifies the value of x as a byte type 
x = bytearray(5)                 # specifies the value of x as a bytearray type
x = memoryview(bytes(5))         # specifies the value of x as a memoryview type 


# THE NUMERIC TYPE AKA NUMBERS

"""There are only three numeric types in python.
These are imediatelly created when you assign a value to them """
x = 1   #int
x = 1.2 #float
x = 1j  #complex

"""To verify the type use "Type()" function"""
print(type(x))

"""" Integers are whole numbers, without a decimal,
they are unlimited in count and can be positive or vegative."""
#Examples:
x = 1
x = 4548095242543552085424352988991
x = -1232

""" Floats or floating point numbers have one or more decimals. they can be positive or negative.
 They can also be scientific numbers with an e or E to indicate the power of 10"""
#Examples:
x = 1.0
x = -6480.94305732
x = 0.434243920
x = 456e5
x = -53840E345
x = 1.0e6

""" Complex numbers are writen with a j as the imaginary part"""
#Examples:
x = 4+6j
x = -1j
x = 5j
print(type(x))

""" You can CONVERT from one type to another with int(), float(), complex() methods"""
x = 1   #int
y = 2.8 #float
z = 1j  #complex

#convert from int to float
a = float(x)

# convert from float to int
b = int(y)

# convert from int to complex
c = complex(x)

# you can not convert a complex to anytype though ):

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))


""" RANDOM NUMBERS. There is no such a thing as random() function in python.
Python uses a built in module* called random to make random numbers. """

import random # If it is a module, you have to import it.
print(random.randrange(1,10))




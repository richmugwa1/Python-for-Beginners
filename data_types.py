
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

"""Casting in python is a way to specify a dataype even if the value was assigned a different data type, we use these constructors int(), float() and str() to do casting in python """
#Example
x = int(1)      #constructs an integer from an integer literal
x = int(2.9)    #constructs an integer from a  float   literal * rounds down to the previous whole number
x = int("5")    #constructs an integer from a  string  literal * the string must contain a whole number

x = float(1)    #constructs a float from an integer 
x = float(5.8)  #constructs a float from a float 
x = float("5")  #constructs a float from a string 
x = float("5.9")#constructs a float from a string representing a float number

x = str(1)     # You can contruct a string from any other data type
x = str(1.5)   # You can contruct a string from any other data type
x = str("Hi")  # You can contruct a string from any other data type 


#THE TEXT TYPE AKA  STRING

""" The sytax is simple. A string is srrounded by either single quotes or double quotes  """

x = "Jon" # is the same as 
x = 'John'
print(x)

"""You can assign a multiline string to a variable using three double quotes or three single quotes"""

x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""" # is the same as 

x = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(x) # The line breaks at the same position as in the code.


""" Accessing a unique character in a string. Remember that Strings are arrays of bytes representing unicode characters. The beauty of Python is that a single character is itself a string with lenght of 1, it makes it easier to access, use square brackets [] to access any element of a string """

a = "Hello World"
print(a[1]) # It gets the element at position(or index) 1. * python starts at index 0

"""Slicing: You can access elements from an index to another. 
Use a colon to get characters from index 2 to index 5(not included)"""

print(a[2:5]) # You get elements until the comma(index 5). * note the coma is not included

"""You can also start indexing from the end of the string by using negative indexes"""

print (a[-5:-2]) # [-5] is the space, [-2] is l but not included. you get Wor.

"""The len() function returns the lenght is a string"""

print(len(a))

"""String Methods(Methods are different from fuctions because they are used by the variables ( variable.method) while functions use the variables(function(variable)). )"""

#strip() method. will remove any white spaces from the begining and the end of a string

a = "  I love you MOM   "
print(a)
print(a.strip())

#lower() method. will return the string in lower case

print(a.lower())

#upper() method. you guessed it right. 

print(a.upper())

#replace() method. will replace specified elements in a string with another string of new elements 

print(a.replace("I","Me")) # It takes two arguements, the old string, the new string

#split() method. will split the string into substrings at every instance of a separator
a = a.strip() #this removes spaes at the begining and the end.
print(a.split(" ")) # This will separate the strings evertime it sees the "space separator"

"""There are about 40 string methods that you can search on the internet and familiarize yourself with"""

"""Check strings. You can check if a cetrain phrase of character is in the string. 
use the keyword "in " or "not in" to do that. """

txt = "I love you mom"
x = "love" in txt
print(x) # it will return a boolean True because it checks if the phrase 'love' is in the value of 'txt' which is true

y = "love" not in txt
print(y) # It will return the boolean False ebecause it checks if 'love' is not in the value of 'txt' with is False

"""String concatenation, to combine two or more strings just use the '+' operator"""
word1 = "I"
word2 = "love"
word3 = "you"
word4 = "mom"

combined = word1 + word2 + word3 + word4 
print(combined)

"""To add space between them, use '+ " "' """
combined = word1  + " " + word2 + " " + word3 + " " + word4
print( combined)

""" To combine a string and a number in one print function, we use the format() method
To do so, we specify where the number/or string should go and put a spaceholde {}. The format method argument will be the content for the spaceholder and it will be formated to work with the print function"""

age = 18
txt = "I am {} years old"
print(txt.format(age))
#the format() method can take an anulimited number of arguments and are delivered in respective placeholders.
age = 30
exp = 12
Apps = 3
rev = "MILLION"
pres= """My name is Richard, I am {} years old, I have been in the industry
for {} years and I have made {} successfull application 
that are currently making {} dollars"""

print(pres.format(age, exp, Apps, rev ))

#If you use the index numbers, it will force the arguments into the desired placeholders.
pres2= """My name is Richard, I am {1} years old, I have been in the industry
for {3} years and I have made {3} successfull application 
that are currently making {0} dollars"""
print(pres2.format(age,exp,Apps,rev)) #See how the order has changed.

"Escape characters in python are characters that save you from writing illegal characters as double quotes inside double quotes"
#Example
#print( "my name is Bond "james" Bond ") #This will give an error
print("my name is Bond \"James\" Bond") #the '\' is an escape character, python can't read it

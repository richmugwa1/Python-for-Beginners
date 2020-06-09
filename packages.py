""" a package is a collection of modules. Pythons has a gread deal of built-in packages. 
Depending on the purpose of the applications. """

# DATETIME
""" datetime is a module to work with dates"""

# The time now
import datetime
x = datetime.datetime.now()
print(x)

# The year and the name of weekday
import datetime
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Create date objects
""" Use the datetime() class constructor of the datetime module
it takes arguments respectively, year, Month, Day, hour, minute, second, mictosecond, tzone
if not specified, the arguments are set to zero and none for timeo=zone """

import datetime

x = datetime.datetime(2020, 5, 17) # datetime() class takes three parameters, year, month, day
print(x)

# The strftime() method
""" to format date and time into readable strings
the srtftime() method takes one argument which is the format """

import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) #This will display the name of the month
print(x.strftime("%A")) # THis will display the name of the weekaday

# reserach on more legal time format codea and have fun. 


# MATH
""" Python has a number of built-in math functions including an extensive math module that 
allows you to perform mathematical tasks on numbers """

# The min () and max() Functions.

x = min(5, 10, 25) # no need to import them because they are built-in functions 
y = max(5, 10, 25)

print(x)
print(y)

# The abs(), pow(x, y) functions
""" abs () returns the absolute positive number ofspecified number """
x = abs(-44.58540)
print(x)

""" pow (x, y) returns x to the power of y"""
x = pow(4,5)
print(x)

# The math module
""" You will have to import it because it is a module. 
It had a gread deal of methods and constants"""
import math
# math.sqrt() method
x = math.sqrt(64)
print(x)

# math.ceil() and math.floor() methods
""" round upwards and downward respectively to the nearest integer"""

x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)

# math.pi constant to display the value of PI (3.14...)

x = math.pi
print (x)

# Reserach more about the math module methods and constants and have fun,

# JSON
""" JSON (Java script object notation)is a syntax used to store and exchange data 
Python has a built in package called json used to work with JSON data"""

# json.loads() method
import json

x = '{"name": "Richard", "age":30, "city":"Montreal"}' # This is a json string.

y = json.loads(x) # Let's parse x
print(y["age"])

# Convert Python object into JSON with json.dumps() method

import json

x = {                   # This is a python object (dict)
    "name": "John",
    "age": "23",
    "country":"USA"
}

y = json.dumps(x) # Convert x into JSON
print(y)

# converible object types.
""" dict, list, tuple, string, int, float, True, False, None
only those can be converted to JSON (Java script equivalent)"""

import json

print (json.dumps({ "name": "Richard", "age":45, "city": "New York"}))
print (json.dumps(["banana", "apple", "cherry"]))
print (json.dumps(("apple", "Banana", "cherry")))
print (json.dumps("hello"))
print (json.dumps(5))
print (json.dumps(56.86))
print (json.dumps(True))
print (json.dumps(False))
print (json.dumps(None))

#All legal datatypes in one example.
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Format the result for readability.
""" using the 'indent' parameter to define the number of indents"""
print(json.dumps(x, indent=4))

""" using separators parameters. 
The deafaut uses commas to separate values 
and colons to separate keys from values"""
print(json.dumps(x, indent=4, separators=(".", "=")))

""" using 'sort_keys' parameters to specify 
if the result should be sorted or not. """

print(json.dumps(x, indent=4, sort_keys=True))

# Regular Expressions
""" Also called RegEx, this is a sequence of characters that make up a serach pattern"""
""" They are used to check if a string contains a specified seeach pattern
The python built-in module for RegEx is called re  """

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes we have a match")
else:
    print("no matches sorry")

# Metacharacters
""" These are characters with special meaning"""
        # []    a set of characters   
        #  \    signals a special sequence, or used to escape special characters
        # .     Any character (Except newline character)
        # ^     Starts with
        # $     Ends With
        # *     Zero or more occurencies
        # +     One or more occurencies 
        # {}    Exactly the specified number of occurencies 
        # |     Either or
        # ()    Capture and group

# Special Sequences
""" the '\' followed by  the following characters: """
        # \A    match if characters present at the begining of the string 
        # \b    match if characters present at the end or beging of the word
        # \B    match if characters present but not at begining nor the end
        # \d    match if string contains digits from 0 to 9
        # \D    match if string contain no digits
        # \s    match if string contains a white space
        # \S    match if string contains no space
        # \w    match if string doesn't contain any word
        # \Z    match if characters are at the end of the string 

# Set
""" characters inside square brackets with special meaning"""
        # [arn]     match if  characters(a,r,n,...) are present
        # [a-n]     match if  characters(lower) betweeen a and n are present
        # [^arn]    match for characters other than (a,r,n,)
        # [1234]    match if digits(1,2,3,4...) are present
        # [0-9]     match for any digit between 0 and 9
        # [0-5][0-9]match for any two-digit number from 00 to 59
        # [a-zA-Z]  match is charcters(lower or upper) betwen a and z are present
        # [+]       match for any + character in the string.(Same for *,-,.,...)

    
# 're' module functions.
""" These are the functions that allow to search a string for a match """
        # findall   list containing all matches

import re

txt = "The tain in Spain"
x = re.findall("ai",txt)
print(x)

x = re.findall("Protugal", txt) #This gives and empty list. No match was found.
print(x)
        # search    match object if there is any match in the string
import re
txt = "The rain in Spain"
x = re.search("\s", txt) # looking for white space in the string
print("The first white-space character is located in position", x.start())

x= re.search("Portugal", txt) # None is returned because there was no match found
print(x)

        # split     list where the string has been split at each match

import re

txt = "The rain in Spain"
x = re.split("\s", txt) #Split at each white space 
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1 ) # control the number of occurencies, here split only at the first occurence.
print(x)
        # sub       Replaces matches with a string.
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2 ) # Control the number of replacement, here is for the first two .
print(x)

# The match object
""" it is an object contraining information about the search and the result """

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) # this is the object

         # .span() is a tuple of the start and the end position of the match
x = re.search(r"\bS\w+",txt) # Search for capital letter S starting or ending any part of the string.
print(x.span())
         # .string  is the string passed into the function
print(x.string)
         # .group() the part of the string that contains the match
print (x.group())

# PIP

""" A quick recap:
Almost everything in python is an object. Meaning it can be created used and resused localy or globaly.

Variables are objects that can contain values
functions are objects that can contain variables, conditions, methods and instructions
Classes are objects that contains a bunch of functions or variables or both, with their properties and methods.
Modules are objects that contain classes, functions, variables, constants and all their methods and properties
Packages contain a bunch of modules"""

""" Pip is a python package manager. With python 3, you have pip included by default

 You can always find python packages from https://pypi.org/.  and use pip to install them packages"""

 # Install package with the commad line:             pip install [packagename] 
 # Uninstall package with the comandline             pip uninstall [packagename]
 # List all available packages with the comand line  pip list


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
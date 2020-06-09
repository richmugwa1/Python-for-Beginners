# ITERATORS
""" An object that contains a countable number of values is an iterator"""
""" do not confuse iterators with lists, tuples, dictionaries and sets objects. 
Those objects are ITERABLE containers from which you can get an ITERATOR."""

# Iterator protocols use the 'iter' and 'next' methods.

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Even a simple string is iterable and can return an iterator

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Looping through an iterable object

""" the for loop basicaly creates and iterator object 
and executes the next method for each loop """

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

mystr = "banana"

for x in mystr:
    print(x)

# Create and iterator.
""" We use the __iter___() and the __next__() methods """
class MyNumbers:            #create the class
    def __iter__(self):     #def
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# SCOPE
""" Scope simply put, states that a variable is only available from inside the region where it is created"""

# x is only available inside myfunc not outside.
def myfunc():
    x = 300 # 
    print (x)
myfunc()

# x can also be accessed from a function inside the primary function.

def myfunc():
    x = 499
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

# A variable created outside a function can be used by anyone.

x = 500

def afunc():
    print(x)
afunc()
print(x)

# The same variable used localy and globally will be treated as two different variables.

x = 460

def fun():
    x =600
    print(x)
fun()
print(x)

# The 'global' keyword will turn a local variable into a global one.

def function():
    global x
    x =300
function()
print(x)

#The 'global' keyword can also be used to make a change to a variable

x = 2020
def myfun():
    global x
    x =2021 #this changes the value of the global variable even if it is inside a local scope.
myfun()
print(x)


# MODULE
""" Module is just a code library. A file containing a set of functions that you want to use"""

# Create a module
""" just save your code with a .py extension, 
I just did in a separate file called mymodule.py """
def greeting(name):
    print ("Hello, " + name) # the function is not called.

# Use a Module
""" just import the module and call the function """
import mymodule
mymodule.greeting("Jonathan")

# Variables in Modules
""" instead of the function, a module can also contain variables of all types"""
"""let's save this in a file named dicmodule.py """
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
""" Now we can use the dictionary"""
import dicmodule

a = dicmodule.person1 ["age"] # we are accessing the age element in the saved dictionary.
print(a)

# Create a module alias
""" use the 'as' keyword"""
import dicmodule as dm

c = dm.person1 ["country"]
print(c)

# Built-in Modules
""" there are several python built-in modules that you can call anytime"""

import platform
x = platform.system()
print(x)

# List all functions or variables of a module
""" use the dir() function to know all the defined functions and variables in a module """

import platform

x = dir(platform)
for a in x: # This is to for readability, otherwise you could just print x
    print(a)

# Import from Module
""" Call this module5.py it contains a function and a dictionary variable"""
def greeting (name):
    print("Hello, " + name)
person1 = {
    "name": "Jean",
    "age": 56,
    "country": "Canada"
}
from module5 import person1 # if we only want to use the dictinary variable of the module.
print (person1["age"])
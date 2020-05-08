# FUNCTIONS
""" Block of code that runs when only called """
""" You pass data as parameters/argumets into a function"""
""" the function will return data"""

#Creating a function
""" 'def' keyword"""
def my_function():
    print (" This is a function") #Nothing will happen if you run this. It is created but not called.
    
#Calling a function
""" function name followed by parenthesis"""
my_function() # Now it can run

#Arguments
""" inside the parenthesis after the function name, you can pass as many arguments (args) as you want
separated by a comma"""

def my_function(fname):
    print(fname + " Obama")

my_function("Barack") # We pass an instance of actual first name to replace the fname placeholder
my_function("Michelle")
my_function("Maria")

""" a function must be called with the correct number of arguments.
if it is expecting two arguments, call it with two arguments. Not less not more"""

def my_function(fname, lname):
    print(fname + " " +  lname)

my_function("Alicia", "Keys") #There have to be just two argumens as defined beforehand

""" *arg AKA arbitrary arguments. Suppose you do not know how many arguments you will need
just add a '*' before the argument name, The function will receive a tuple of arguments 
and it will access them accordingly"""

def my_function(*musicians):
    print( " the most famous is " + musicians[3]) # the index the the function will print

my_function("Celine", "Beyonce", "Lenon", "Winnie","ub40","Charles")

"""  kwargs AKA Keyword Arguments. You can call a function with precised key for the passed arguments.
This way the order of argumennts does not matter"""

def my_function(ch5,ch2,ch4,ch1,ch3):
    print (" My favorite TV channel is " + ch4) #ch4 name will be printed no matter what order

my_function(ch5 = "CNN", ch4 = "FOX", ch1 = "MTV", ch3 = "BBC", ch2= "BET" )

""" **kwargs AKA Arbitrary keyword arguments. Suppose you do not know how many keyword arguments
to pass in the function definition, add '**' before the argument name
this way the function will receive a dictoinary of arguments and access them accordingly"""

def my_function(**ch):
    print(" My favorite TV channel is " + ch["ch4"] )
my_function(ch1 = "MTV", ch2 = "BET", ch3 = "BBC", ch4 = "FOX", ch5= "CNN") #dictionay key-value pairs

""" you can precise a default argument/ parameter value in the function definition
so that if you call the function without an argument, the default will be used"""

def my_function( country = "Canada" ):
                print ("I am from " + country)
                
my_function("USA")
my_function("Mexico")
my_function()

#Lists as arguments
""" Not just lists but any data type you send as argument will pass through the function as same datatype"""
def my_function(food):
    print(food)
    print(type(food))                                     # show the type
fruits = ["apple", "banana", "cherry"]                    # lists as arg
fruits = ("apple", "banana", "cherry")                    # tuple as arg
fruits = {"apple", "banana", "cherry"}                    # set as arg
fruits = {"apple" : 50, "banana" : 100, "cherry" : 59 }   # dict as arg
my_function(fruits)

# Return a value
""" if you want a function to return a value, use the 'return' statement"""
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))

# Pass statement
""" a function can't be empty. use the 'pass' statement to avoid getting an error"""
def function():
    pass

# Recursion
""" a function can call itself. Be careful to not make a function that will never end and uses a lot of memory and processing power
In this example, the number of recurions 'k' decrements by 1 everytime a recursion occurs

*Fasten your belt it is gonna be tricky yo calculate this in your head"""
def tri_recursion(k):                       # we define a function called 'tri_recursion' with argument 'k' number of recursions
    if k > 0:                               # a condition that keeps k greater than 0
        result = k + tri_recursion(k - 1)   # a new variable 'result' whose value is the sum of  k and our function, when k is decremented by 1
        print(result)                       # print the variable 'result'
    else:
        result = 0                          # When k is less than 0, the variable 'result' will be 0
    return result                           # the tri_recursion() function returns the value of the variable 'result'

print(" \n\n Recursion Example Results")
tri_recursion(6)                            # We call the function giving k the value of 6, meaning 6 recursions of the function.


# LAMBDA FUNCTIONS

""" Sometimes you will want to use an anonymous function for a short period of time, lambda funtion is the solution"""
""" the syntax is  lambda arguments : expression """
""" the expression is executed and the result is returned"""

x = lambda a : a + 10
print(x(23)) # the argument is a. The lambda function is initially called in python, no need to call it again. Just pass the arguments

""" many arguments with lambda function"""

x = lambda a, b, c : a + b + c
print(x(2, 4, 6)) # all arguments are passed respectfully as they were declared

""" using lambda inside other functions. Here goes the power of lambda functions"""
def a_function(n):
    return lambda a : a*n
double = a_function(2) # the argument 'n' of the main function is passed
triple = a_function(3)
print(double(10)) # the argument 'a' of the lambda function is passed 
print(triple(5))


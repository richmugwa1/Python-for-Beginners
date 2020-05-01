

#Indentation
if 5>2:
  print("Five is greater than two")
  print("Five is greater than two")
""" You can put the spaces you want to indent as long as you keep the consistency.
Try to put one more space at the last print function line and you will see by yourself. """



# Comments
#yeah funny we have been doing this, huh!
""" yeah, anytime I want to create a whole
paragraph, I use these triple quotes
or multline string as geeks call it
so that python ignores everything"""
print("I hope you ignored the other comments")



# Variables
x = 5
y = "Hello World!"

"""These dudes are like containers to store a value inside.
A variable is created at the moment you assign a value to it.
Python will know it is a variable so chill, no need to declare it or watsoever."""

print(x,y)

                                #.........variable type..............

x = 8   #This sets the value of variable x to an INTIGER (int) type
x = "Brother" # This resets the value of x to a STRING (str) type
"""Variables don't necessarily need to be declared with any particular tye
and can even change the type after they have been set"""
print(x) # Funny huh!, x that was set to be 8 is now called Brother!

                                #...........strings .............

x = 'John'
x = "John"
""" This is basically the same thing.
A string variable can use a single quote or a double quote"""
print(x)

                                #........Variable Names...............
myvar = 4
my_var = 4
_my_var = 4
myVar = 4
MYVAR = 4
myvar2 = 4
""" These variables have legal names. They are all different variables.
The following are illegal names especially when
you try to start with a number, put a hyphen or space to separate characters of a name"""

#2myvar = 4 # Never start with a number, numbers can go in between or at the end
#my-var = 4 # Never put a hyphen, instead use an underscore to separate characters
#my var = 4 # Never use space as separator, use an underscore (_) instead

"""Variables in python are case sensitive,
so the followng varibales are STRICTLY  3 different variables"""
myvar = 4
MYVAR = 4
mYvaR = 4

                                #..........Multiple Variables, Multiple Values.....
x, y, z = "Orange", 5 , "Banana"
print(x)
print(y)
print(z)

""" This is the time you have to undersand and respect the word "respectively"
If the variables are separated with a coma,
their RESPECTIVE values are separated ith a coma.
For fun Try to miss some values and let me know what you get"""

                            #.......Multiple Variables, one value and vice-versa....
x = y = z = "Oranges"
f = "apple", 7
o = "Mangoes"

print (x)
print(y)
print(z)
print(f)

""" You can assign one value to a bunch of variables
or a bunch of values to one variable, note that the later option's output (f)
is in parathesis,we will discuss this a little bit futher"""

                            #.......Output.............
"""Funy we have been outputing stuffs since line one. Well,
we use the print function* the syntax is print followed by pranhesis
in which you put the variable or multiple variables separated by the comas"""

print(x, y, z, f)

""" Instead of outputting a variable, you can output just a text in a form of a string.
The print function is always ready"""

print("This is a text, just printed out of no where. It is in a form of astring")

""" You can also create new lines and paragraphs in the print function as you want.
Use '/n'  to do that"""

print("This is a text, just printed out of no where"'\n'"It is in a form of astring")

"""You can also output text and a variable in one print function, use a + sign"""

print ("I love to eat an " + x + " When I am happy")

""" You can even use the + sign to add virables if they are of the same type"""

print(o + " " + x )# The double quotes are just text, I wanted space to separate them ):

""" I guess I do not need to mention that is your variables are numbers,
the + sign will just add them. This language can't help with maths."""

print(myvar + my_var) # We created these variables in the upper section about "Names"


                        #..........Global Variables..............
"""Let's face this, the term FUNCTION must be in your toolbox.
Because every block of your python code will be delivered inside an envelope.
That evelope is the function. All variables created outside os the envelope are called global variables.
The can be used inside the function or outside the function.
Think of it as a public bathroom.
Both he people in the compound and outside can use them."""

x = "Great" # This is a variables outisde of a function below

def myfunc():
    print("I am doing" + x)
myfunc() #The function considers the x outside because it has no other option

"""Let's create a variable with the same name inside the function and see
(remember to comment the function above for debuging )"""

x = "Great" 

def myfunc():
    x = "Owesome"
    print("I am doing " + x)
myfunc() # This function resets the outside (GLOBAL)x to the inside (local)x values.
print("I am doing " + x) # This output reconsiders the x outside the previsous function

""" You can use the GLOBAL keyword to keep a variable usable
both inside and outside a function, Use the GLOBAL KEYWORD """

def myfunc():
    global x # set this variable to be used globaly
    x = " FINE"
    print(" I am advancing" + x)
myfunc()
print("Yes I am " + x) # the x in the function is recognised even outside because of the global keyword
    
""" You can change the value of a global variable inside a function"""

x = "super"
def myfunc():
    global x # This sets x to become usable even outside of the function
    x = "My Friend" # This changes the value of x to MY FRIEND
    print ("You are " + x)
myfunc()
print(x + " you are!") # It will collect the new value of x

""" If you lan to reuse a variable, declare it global before you assign it a value,
the opposite will put you in trouble. Test it and tell me"""




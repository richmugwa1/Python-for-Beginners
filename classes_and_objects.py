#Python is an object oriented language, meaning that almost everything we have been seeing so far is an object.
#A class is an object constuctor, a blueprint for crwating objects.

"""use the keyword 'class' to create a class"""

class MyClass: #Note that there are no parathesis as we used to have for the functions.
    x = 5 # in this class the variable x will always be equal to 5
""" Now we can use the class called 'MyClass' to create an object"""

p1 = MyClass() # Here we create a object called p1 using MyClass and print the value of x 
print(p1.x) # note the object.variable notation, the output is the value of x


#THE __init__() FUNCTION

# this is a python built-in function that is automatically initiated everytime a class is called.

class Person: # First we create a class called Person.
    def __init__(self, name, age): # Then we define the __init function___ whose first argument is the class itself.
        self.name = name # Here goes instuctions of what the function will do.
        self.age = age # We are using the class to create new opjects "name" and "age"

p1 = Person("George", 36) # we create a new object  out of the fucnction 'p1' using our original class.

print(p1.name) # the __init__() function is called automatically everytime the class 'Person' 
print(p1.age)  # is bein called to create a new object. 

# OBJECTS METHODS
""" objects can also contain methods. They are functions that belong to the object in question"""
"""Let's insert a method (in this case is a funciton) that prints a greeting. 
and execute it on the 'p1' object"""

class Person: # We create a class called 'Person'
    def __init__(self, name, age): # As we say it, define the class's __init__ function
        self.name = name # Create object 'name' using 'Person' class in the form of 'self'.
        self.age = age   # Create object 'age' using 'Person' class in the form if 'self' 
    
    def myfunc(self): # Create a new function 'myfunc' taking itself as argument 'self'
        print("Hello My name is " + self.name ) # use the 'name' object as a METHOD 
p1 = Person("Joel", 76) # Create a new object 'p1' using the orginal class
p1.myfunc() # Call the newly created function. It is not automatically called as the __init__ function. 

# THE SELF PARAMETER/ARGUMENT
""" The 'self' parameter is a reference to the curent instance of a class. 
It is used to access variables that belong to the class"
"""
"""it doesn't necessarily have to be called 'self', you can call it 'tomatoes' if you like,
as long as it is the first argument of any function inside the class"""

class Person:
    def __init__(tomatoes, name, age):
        tomatoes.name = name
        tomatoes.age = age
p1 = Person("Ben", 85)
print(p1.name)
print(p1.age)
       
# MODIFY OBJECT PROPERTIES
p1.age = 59
print(p1.age)

# DELETE OBJECT PROPERTIES
""" use the 'del' keyword"""
del p1.age
print(p1.age) # You will see this error AttributeError: 'Person' object has no attribute 'age' because it is deleted

""" the 'del' keyword can also delete objects"""

del p1
print(p1.age)

# PASS
""" If for some reason you want to leave the class empty, use the  'pass' statement"""
class myclass:
    pass

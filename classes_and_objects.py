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
#print(p1.age) # You will see this error AttributeError: 'Person' object has no attribute 'age' because it is deleted

""" the 'del' keyword can also delete objects"""

del p1
#print(p1.age)

# PASS
""" If for some reason you want to leave the class empty, use the  'pass' statement"""
class myclass:
    pass

# INHERITANCE

""" python uses inheritance to define a class that inherits all the methods and properties 
from another class """
# parent class/ base class, the class being inherited from.
# Child Class/ derivered class, the class that inherits.

# CREATE A PARENT CLASS
""" Just create any class"""
class Person:                                # This is the class containing names of a person.
    def __init__(self, fname, lname):        # Define the built-in self calling __init__ function
        self.firstname = fname               # The class property 'firstname'
        self.lastname = lname                # The class property 'lastname'
    
    def printname(self):                     # The class method 
        print(self.firstname, self.lastname) # The only method here is to print
x = Person("Jean", "Jack")                   # A new object created using the class.
x.printname()                                # Executing the method using this new object

# CREATE A CHILD CLASS
""" send the parent class as a parameter"""
class Student(Person):       # The Student class inherits properties and methods of the Person class
    pass                     # Since we do not want to change the properties or methods of the parent

y = Student("Bob", "Marley") # A new object created using the 'student" class, it takes the parent's properties
y.printname()                # Executing the parent class method using the newly create object.    

# ADD THE __init__() FUNCTION TO THE CHILD CLASS
""" 
from the moment we give a achild its __init__() function,
it starts behaving independently of the parent and there is not inheritance
 """

class Student(Person): # If you remove the parent as argument, it will still work
    def __init__(self, fname, mname, lname): # The child will have its own properties and methods
        self.firstname = fname # Child's own properties
        self.lastname = lname #Child's own property
        self.middlename = mname #Child own property
    def print_a_name(self): # Child's own method
        print(self.firstname, self.middlename, self.lastname) #Child's own method 
pres = Student("Barack", "Hussein", "Obama") # new object created using child class
pres.print_a_name() #Executing the method using the newly created object.

""" Keep the inheritance of the __init__() function of the parent. """
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) #This makes the child inherit the __init__() of the parent
    
    def print_b_(self):
        print(self.firstname, self.lastname)

z = Student("Johnny", "Deep")
z.print_b_()


# THE super() FUNCTION
""" It is used to force a child Keep the inheritance 
of both properties and methods of the parent"""

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) # no need to say the name of the parent anymore
w = Student("Alicia", "Keys")
w.printname()

# ADD A PROPERTY & A METHOD
""" To get the child have its own properties and methods
but also inherit from the parent's properties and methods
you can add properties and you can add methods too"""
class Student(Person):                       # Create a child class with the parent as argument.
    def __init__(self, fname, lname, year):  # Add a new argument 'year' to the child's __init__
        super().__init__(fname, lname)       # Force the child's inheritance from the parent
        self.graduationyear = year           # Add new properties, unique to the child, that match the new arguments
    def welcome(self):                       # Define a new method. Different name than the parent. Otherwise the child will override.
        print("Welcome", self.firstname, self.lastname," to the class of ", self.graduationyear) # What the new method does.
w = Student("Alrick", "Brown", 2008)         # Create a new object using the child class.
w.welcome()                                  # Execute the new method using the newly created object. 


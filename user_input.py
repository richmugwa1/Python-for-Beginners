# INPUT METHOD.
""" input() will ask a user to enter values  """

username = input("Enter Username:  ") # Python stops when it sees the input
print("Username is : " +username)

# STRING FORMATING
""" To make sure the string displays as expected we use the format() method """ 
# use {} in the string as a place holder where values will come from a database or from a user input
# run the values through the format() method

price = input("enter the starting price in USD: ")
txt = "Your starting price is ${}, let's begin"
print(txt.format(price))

# specify how to convert the values
price = float(input("enter the starting price in USD: ")) # We used a float constructor to force the input to be floar
txt = "Your float price is ${:.2f}, let's begin" #format price to be displayed as a decimal number with two floats.
print(txt.format(price)) 

# Multiple values
""" You can output an unlimited number of values depending on the application you are creating"""
item_name = input("Item: ")
qty = float(input("Quantity in kg: "))
itemno = int(input("item #: "))
price = float(input("Price: "))

order = " \n\nPlease confirm your order of :\n\n-{:.1f} Kgs of {}.  \n-It will cost you ${:.2f}\n-Product number: {}\n\n  "
print(order.format(qty,item_name,price,itemno))

# Index numbers
""" You can indicate the order with index numbers in the curly brackets"""

order2 = " \n\nPlease confirm your order of :\n\n-{0:.1f} Kgs of {1}.  \n-It will cost you ${2:.2f}\n\n*Product number: {3}\n\n  "
print(order2.format(qty,item_name,price,itemno))

# Named indexes
""" you can also put names in the curly brackets """
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))


# HANDLING ERRORS

""" python let's you test for errors, handle them and execute blocks of code
We use the 'try' , 'except', 'finally' blocks"""

# try, except

try:
    print(x) #this would yell an error because x is not defined as an object
except:
    print("an exception occured") # When try block raises an error, the except block will be executed

# try except else
try:
    print("Hi") # This is no error at all
except:
    print(" That should have worked, what is wrong?") #not ececuted because there is no error
else:
    print("nothing went wrong, it works") # Excecuted since no errors were raised

# try except finally
try :
    print(x) #This would normaly raise an error
except:
    print("Ooops, that x though!!!") # Executed because try raised an error
finally:
    print("Whatever. Wether try raises an error or not, I will just be executed") # Excecuted no matter what

# Useful to continue the program even if some erroes are raised
"""try:
  f = open("demofile.txt")
  f.write("Lorem Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()"""

# raise
""" you can use the 'raise' keyword to raise an error
you define the type of error you want to raise """

x = int(input("enter a positive number"))
if x < 0:
    raise Exception("sorry no negative numbers allowed")
    
elif x is str:
    raise TypeError(" only integers allowed")
    
else:
    print(" Thanks your number is :" , x )
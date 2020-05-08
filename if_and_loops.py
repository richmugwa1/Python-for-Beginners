# IF STATEMENTS

""" Python supports the usual mathematical local conditions"""
# ==    equal
# !=    not equal
# <     less than
# >     greater than
# <=    less than or equal to
# >=    greater than or equal to


#if
"""an if statement uses the 'if'" keyword. and mostly use the above logical conditions""" 
a = 33
b = 300
if b > a:
    print("b is greater than a") # notice the indentation of this line

#elif
""" the 'elif' keyword if used after the 'if' keyword to create a new condition in the case
the first one is not True"""

a = 33
b = 33
if b > a:
    print(" b is greater than a ")
elif a == b:
    print(" b is equal to a")

    
#else
""" the 'else' keyword catches anything that is not cought by all previous conditions"""
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif b == a:
    print( " a and b are equal")
else:
    print(" a is greater than b")

""" You can aslo have an 'else' without an 'elif' """
if a > b:
    print(" a is greater than b")
else:
    print(" a is not greater than b")

#Short hand if
""" when there is one statement to execute"""
if a > b: print("a is greaterrr than b") # you just bring the print function on the same line as the statement.

#Short hand if ... else
""" when there is only one statement for 'if' and one for 'else' 
The techniwue is called Ternary operators ot conditional expressions"""
a = 2
b = 330
print("a is greater") if a > b else print("b is greater") # note that the colons disappear

""" you can also have multiple 'else' statements on the same line """
a = 300
b = 300
print("A") if a > b else print("B") if b > a else print("A = B")

#And
""" the 'and' keyword is a logical operator that combines two conditional statements"""

a = 200
b = 33
c = 500

if a > b and c > a:
    print ("both conditions are true")

#Or
""" The 'or' keyword is also a logical operator used to combine conditional statements"""
a = 200
b = 33
c = 500

if a > b or a > c:
    print("At least one of the conditions is true")

#nestedif
""" you can put an if statement inside another if statement. Thery are called nested if statements"""
x = 16
if x > 10:
    print( 'Above ten,')
    if x > 20:
        print("and also above twenty!")
    else:
        print(" but not above twenty")
else:
    print(" Below ten !")

#The pass statement
""" if statements can't be empty, it you want to leave it hanging, use the pass statement to avoid errors"""
a = 33
b = 200
if b > a:
    pass #nothing happens but also no errors displayed.


# WHILE LOOPS
""" The while keyword creates a loop that execute statements as long as a condition is true"""

i = 1 # relevant variables must be ready. Here i is an indexing variable
while i < 6:
    print(i)
    i += 1 # if you do not increment i, the loop will go on forever.

#Break
""" The break statement will stop the loop even if the condition is true"""

i = 1
while i < 6:
    print(i)
    if i == 3: 
        break
    i += 1

#Continue
""" the continue statement will stop the current iteration and continue the next"""
i = 0 
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)
    
#Else
""" The else statement will run a bloc of code if the condition is no longer true"""
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("Input is invalid")
    
# FOR LOOPS
""" the for loops iterate over a sequential dataype as lists, tuple, set, dictionaries and strings
it will execute a bloc of statements, once for each item in list, tuple, set, dictionary or string"""

fruits = ["apple", "banana", "cherry"]
for x in fruits: # No need to set an index variable set beforehand as we did for while loops
    print(x)

""" Looping through a string """
for x in "banana":
    print(x)

#Break
""" break will stop the iteration when a precised item is found"""
fruits = ["apple", "orange", "cherry", "banana", "pineapple", "mango"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    
    
""" when break comes before print, the pecised item is excluded"""
for x in fruits:
    if x == "banana":
        break
    print(x)
    
#Continue
""" will stop at the precised iteration and jump to the following item"""
for x in fruits:
    if x == "banana":
        continue
    print(x)
    

#Range() function
""" The function range() will return a sequence of numbers from 0 by default and increments 1 bydefault
until the specified value is reached"""
for x in range(10):
    print(x)

"""  you can precise the starting value in a range by adding a it as first argument(or parameter)"""
for x in range(4,10): # 4 is the starting value, 10 is the ending value
    print(x)

""" You can increment to a precised number instead of the default. Preccise it as the third argument"""
for x in range(4, 20, 2): # 2 is the new increment value
    print(x)

# Else
""" else keyword will execute a bloc of code when the loop finishes"""
for x in range(2,15, 3):
    print(x)
else:
    print( "There you go")

#Nested loops
"""Loops inside loops. The inner loop will be executed for each iteration of the outer loop """
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

        
#Pass statement
""" for can't be empty but for somereason if you want to leave it empty, insert a pass statement
to avoid errors"""
for x in [0, 1, 2]:
    pass
    
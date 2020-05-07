"""Python has 4 COLLECTION TYPES"""

# List a collection which is ordered and changeable. It allows duplicate members
# Tuple is a collection which is ordered and unchangeable. It allows duplicate members
# Set is a collection which is unordered and unindexed. No duplicate members allowed
# Dictionary, a collection which is unordered, changeabe and indexed. No duplicate members.

#LIST

""" Ordered, Changeable, Duplicates allowed, written in square brackets []"""
this_list = ["apple", "banana","cherry" ]
print(this_list)

#Access
""" Use the index number. * python indexes starting from index 0"""
print(this_list[1]) # Returns banana because it is at index 1
""" Negative indexing, -1 is the last item of the list, -2 is the second last,..."""
print(this_list[-1]) # Returns cherry
"""spcify a range of indexes by specifying where to start and where to end. 
This creates a new list."""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # The end index is not included 
""" By leaving out the sart index, the range starts at the first item which is index 0"""
print(thislist[:4]) 
""" By leaving out the end index, the range will go to the end of the list"""
print(thislist[2:])
"""Specify negative indexes if you want the range to start from the end of the list"""
print(thislist[-4:-1]) # -1 is not included because it is the end index

#Change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "baby banana"
print(thislist)

#Loop through a list
""" We will learn about for loops later but check out this code"""
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x) #this prints each item separately

    
#Check if an item exists
"""We use and if statement and the 'in' keyword """
if "apple" in thislist:
    print("yes, 'Apple' is in the fruits list")

#Lenght
""" We use the len() function as we saw for strings"""
print(len(thislist))

#Add items
""" We use the append() method. to put an item after the last item"""
thislist.append("orange")
print(thislist)
""" We use the insert() method. to add an item at a specified index"""
thislist.insert(1, "orange") # first argument is the index, second argument is the new item.
print(thislist)

#Remove items
""" We can use many ways, for instance use the remove() method. You specify the value"""
thislist.remove("banana")
print(thislist)

"""the pop() method. removes an item at a specified index or the last item if index not specified"""
thislist.pop() 
print(thislist)

"""the 'del' keyword will delete an item at a specified index"""
del thislist[0]
print(thislist)

""" the 'del' keyword can also delete the whole list """
del thislist

""" the clear() method. empties the list """
this_list = ["apple", "banana", "cherry"]
this_list.clear()
print(this_list)


#Copy a list
""" We use the copy() method. if you do list1 = list2, it won't be a copy because changes in list1 will keep affecting list2. Always user the copy() method."""

list1 = ["apple", "banana", "cherry"]
list2 = list1.copy()
print(list2)

#Join two lists
""" it can be done several ways, let's start by usinng the '+' sign"""
list1 = ["a","b","c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

""" we can also append all items from list2 to list1 one by one"""
for x in list2:
    list1.append(x)
print(list1)

""" Or you can simply use the extend() method. It adds elements from one list to another"""
list1 = ["a","b","c"]
list2 = [1, 2, 3]
list1.extend(list2) # we extend the list1 with all the elements of the list2
print(list1)

#The list() constructor
""" It can be used to make a  list """
newlist = list(("apple", "banana","cherry")) # note the double brackets.
print(newlist)

#List methods.
""" It is better to familiarize ourselves with the following methods because they are used on 
almost all array dataypes in python. They are eleven.
Here is a trategy. Get the first letter right because most code editors propose you the method after you type the first letter we have ' a, c, c, c, e, i, i, p, r, r, s"""

# append()  to add items to the list
# clear()   to empty the list
# copy()    to copy a list 
# count()   to count the number of elements with the specified indexes
# extend()  to add items to the end of the list or at a certain index
# index()   to see the index of a specified item
# insert()  to add an item at a specified position
# pop()     to remove an item at a specified position
# remove()  to remove the specified value
# reverse() to reverse the order of the list
# sort()    to sort the list


#TUPLE

"ordered, unchangeable or immutable, duplicate members allowed"
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
print(thistuple)

#Access
""" As in lists, use the index in []"""
print(thistuple[1])
print(thistuple[2:5])

#Change the values
""" Well you can't. However, you can construct a list from a tuple and change 
the values of the list and construct it back to tuple"""
thislist = list(thistuple)
thislist[1] = "baby banana"
thistuple = tuple(thislist)
print(thistuple)

#Check if an item exist
""" As we did for lists, we is 'if' statement and 'in' keyword"""
if "cherry" in thistuple:
    print("Yes, We have got cherry")
    
#Tuple length(How many items in it)
""" same as in list we use the function len() """
print(len(thistuple))

#Add items
""" You can't. You can use the the list trick stated above though"""

#Create a tuple with one item
"always put a coma after that item, otherwise python won't know if it is a tuple"
newtuple = ("carrot",)
print(newtuple)

#Remove items
""" You can't, they are tuples remember. construct a list from them before manipulating their content"""

#Join two tuples
""" Use a + sign"""
tuplecomb = thistuple + newtuple
print(tuplecomb)

#tuple() constructor
""" used to create new tupples"""
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#Tuple Methods
""" there are only two methods"""
print(thistuple.count("apple")) # 'count' returns how many time a specified value is present
print(thistuple.index("cherry"))# 'index' returns the index or position of a specified value


#SET

"""Unordered, unindexed, unchangeable, no dulpicate members allowed, a set is writen in
curl brackets {}"""
myset = {"banana", "apple", "cherry"}
print(myset)

#Access
"""You can not access set items by indexing because they are unordered and have no indexes
You can loop through elements of the set with a for loop or use the in keyword"""

for x in myset:
    print(x) #Don't be surprised about the order in which it is printed. A set is unordered.

""" Check if 'banana' is present in the set using the in keyword"""
print("banana" in myset) # You get a boolean True because banana is present in the set

"""Check if 'banana' is present in the set using the if statement"""
if "banana" in myset:
    print("yes banana is in the set")
    
#Change items
""" Well you can't. You can however add and remove items"""

#Add items
""" Use the add() method. if is one item or update() method. if it is many items .
if you use the update(), add all the items as a list, otherwise update will break every character"""
myset.add("mango",) # test if you can use the add() method to add more items
print(myset)

myset.update(["goyava", "pineapple", "kiwi"]) # t* notice the square brackers[] with the update method
print(myset)

#Get the lenght
""" Well u guessed it, use the len() function"""
print(len(myset))

#Remove an item
"""Two methods involved: the remove() method. and the discard() method."""
myset.remove("goyava") # if the item you remove does not exist, remove() will raise an error
print(myset) 

myset.discard("banana") # if the item to remove does not exist, no error is raised with discard()
print(myset)

""" You can also use pop() method. as in lists but since sets are neither ordered nor indexed
it will remove the last item but you won't know the item that gets removed
The returned value of pop() is the removed item"""

myset = {"banana", "apple", "cherry"}
x = myset.pop()
print(x)
print(myset)
""" As seen for the lists, The clear() method epties the set """
    
thisset = {"yoga", "heavyweight", "jogging"}
thisset.clear()
print(thisset)

"The 'del' keyword will delete the set completely"
del thisset
#print(thisset) # You get an error that this set is not defined, because it is gone

#Join two sets
"""there are several ways to do this, you can use union() method. which will generate a new set
or use update() to insert items from one set into another. Note that all duplicate items will be removed. Sets do not allow duplicates """

set1 = {"mango juice", "apple juice", "peach juice"}
set2 = {"mango", "apple", "peach"}
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

#The set() constructor
""" To create a set"""
newset = set(("apple", "banana", "cherry")) # note the double round brackets
print(newset)

# Set methods 
""" the tip is to know the first letter, most code editors as jupyter notebooks will give you 
insightful methods recommendations here we have a,c,c,d,d,d,i,i,i,i,i,p,r, s,s,u,u"""
# add()                         to add items to the set
# clear()                       to empty the set
# copy()                        to copy a set
# difference()                  to return a set of difference between two or more set
# difference_udate()            to remove items in this set that are also included in another specified set
# discard()                     to remove a specified item, no error if the item does not exist
# intersection()                to return a set that is an intersection of two other sets
# intersection_update()         to remove items in this set that are not present in other specified set
# isdisjoint()                  to check if two sets have an intersection or not
# issubset()                    to check if another set contains this set or not
# isuperset()                   to check if this set contains another set ot not
# pop()                         to remove items from the set without knowing which
# remove()                      to remove a specified item from the set, error if it does not exist
# symetric_difference()         to return a set containing the symetric difference between two sets
# symetric_difference_update()  to add the symetric difference of this set and other sets
# union()                       to return a new set that adds two or more 
# update()                      to add items from one set to another without creating a new set



#DICTIONARY



""" Unordered, Changeable and indexed, they are written in curly brackets {} and they have keys and values"""
thisdict = { 
    "name": "john",
    "age": 40,
    "status": "married"
}
print(thisdict)

#Access
"""Access a dictionary item by reffering to its "key" name"""
print(thisdict["name"]) #note the square brackets that used to represent indexes in lists

""" You can also use the get() method"""
print(thisdict.get("age"))

#Change values
"""You can change the value of an item by referring to its key name"""
thisdict["status"] = "divorced" #note the []
print(thisdict)

#Loop thourgh a dictionary
""" the for loop through a dictionary will return the key name"""
"""for x in thisdict:
    print(x)"""
    
"""To return the values here is a method, use []"""
for x in thisdict:
    print(thisdict[x]) #This prints all values one by one

"""Or use the values() method.. to rerun the values"""
for x in thisdict.values(): # (: year :) this is handy, we will see that in the for loops, stay tuned
    print(x)

""" You can also return both keys and values with the items() method"""
for x in thisdict.items():
    print(x)

#Check if a key exists in the dictionary
print("age" in thisdict)
"or you can use the if statement"
if "age" in thisdict:
    print("Yes the key called Age is present in the dict")

# Length:(How many items, key-value pairs ) of a dictionary
'''well we use len() function as usual'''
print(len(thisdict)) # it means there are three key-value pairs.

#Adding items(key-value pair)
""" We use a new index key and assign a value to it"""
thisdict["city"] = "Toronto"
print(thisdict)

#Removing items
""" use the pop() method with the key specified to remove the whole item"""
thisdict.pop("age")
print(thisdict)

"""the popitem() method will remove the last insertred item"""
thisdict["profession"] = "driver" # We are adding item
print(thisdict)
thisdict.popitem() # This will remove the recently added item
print(thisdict)

""" The del keyword removes items at specified key name"""
del thisdict["city"]
print(thisdict)

"""The del keyword can also delete the dictionary completely"""
del thisdict
"""print(thisdict)""" # Error because it does not exist anymore

""" The clear() method. empties a dictionary as for lists and sets"""
dict1 = {
    "name": "John",
    "age": 50,
    "profession": "driver"
}
dict1.clear()
print(dict1)

#Copy a dictionary

""" We use the copy() method."""
dict1 = {
    "name": "John",
    "age": 50,
    "profession": "driver"
}

copy_dict1 = dict1.copy()
print(copy_dict1)

""" Or use the function dict() """
copy_dict1 = dict(dict1)
print(copy_dict1)

# Nested Dictionaries
""" You can put many dictionaries in one dictionary, they are called nested dictionaries"""

family = {
    "parents": {
        "mother": "Joanne",
        "father": "Bruno"
    },
    "brothers": {
        "young": "Bruno",
        "elder": "Josh"
        
    },
    "sisters": {
        "lastborn": "kyla",
        "elder": "Baila"
    },
    "myself": {
        "me": "carine"
    }
}

print(family)

""" or you can create dictionaries and nest them later in one dictionary """
parents= {
        "mother": "Joanne",
        "father": "Bruno"
}
brothers= {
        "young": "Bruno",
        "elder": "Josh"
}
sisters =  {
        "lastborn": "kyla",
        "elder": "Baila"
},
myself = {
        "me": "carine"
}

family = {
    "parents": parents,
    "brothers": brothers,
    "sisters": sisters,
    "myself": myself
}
print(family)

#the dict() constructor
""" You can create a dictionary using the dict() constructor function"""
newdict = dict(name = "JOhn", age = 50) # note that we single round brackets only, and the key can't be string literals
print(newdict)

#Dictionary methods
""" as for the previous colletion data_type, the trick is to memorise the first letter, 
python text editors will give you methods suggestions as you type. dictionaries have : c, c,f,g,i,k, p, p, s,u,v  """

# clear()       to empty the dictionary
# copy()        to copy a dictionary   
# fromkeys()    to create a new dictionary with specified keys and value
# get()         to return a value of a specified key
# items()       to return a list containing a tuple for each key-value pair
# keys()        to return a list containing the dictionary keys
# pop()         to remove item with specified key
# popitem()     to remove the last inserted item
# setdefault()  to return value of specified key, if no key, returns the key of specified value
# update()      to add specified key-value pairs
# values()      to return a list of all values of the dictionary


#ARRAYS
""" These are special variables because an array variable can contain multiple values"""

""" Unlike other languages, python doesn't have built-in support for arrays
in order to work with arrays, you will need to import a LIBRARY. NumPy library is the most used
open source python library hat supports arrays. We will see numpy later."""

"""That bein said, you can use lists as arrays """
#example
cars = ["Ford", "Volvo", "BMW"] # is a list but also an array. It stores many indexed values in one variable.
# each list is an array but each array is not a list, because as you may see with NumPy pibraly, unlike lists
# ARRAYS CAN HAVE UNLIMTED DIMENTIONS.
# arrays can use the list methods.
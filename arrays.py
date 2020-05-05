"""Python has 4 types of array (COLLECTION TYPES)"""
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
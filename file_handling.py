# FILE HANDLING
""" The key function is the 'open()' function """
""" Methods are 'r' for reading (default) 'a' for appending 'w' for write 'x' for create """
""" You can also specify 't ' if it is a text file (default) or 'b' if it is a binary file """

""" !Please go on and create some files in the folder you are working with 
so that we can manipulate them """

# Open function

f = open("demofile.txt") # If the file doesn't exist it will yell ana error.
""" or """
f = open("demofile.txt", "rt") # no need to specify 'r' or 't' because they are default files.

# Read method
print(f.read()) # reads the whole file 
f = open("demofile.txt")
print(f.read(3)) # reads the first five characters of the file
f.close() # This closes the file opened in the f object
a = open ("demofile.txt", "r")
print(a.readline()) #Read the first line only

for x in a:     #This loops through the content of the text file,  line by line
    print(x)

a.close() # This closes the file opened with the a object

# Write 

e = open("file2.txt", 'a') #The 'a' is the append parameter, lests you add more lines to existing ones. 
e.write("Now the file has more content")
e.close() # Always close a file before more operations, it saves the commands.

e = open("file2.txt")
print(e.read())

f = open("file3.txt", "w") # The 'w' is the write parameter, lest's you replace the existing lines
f.write("The original text will be lost in this new text\nbecause of the write mode") 
f.close()
f = open("file3.txt")
print(f.read())

# Create 
""" use parameter 'x'  or parameter 'w' in the open function"""
newfile = open("newfile2.txt", "x") # an empty file is created. It would yell an error if it existed.
newfile.write(" Hi, I am the first text on this file")
newfile.close()


a = open("newfile2.txt") 
#print(a.read())

newfile = open("newfile.txt", "w") # an empty file is created. No error is yield if the file existed.
newfile.write(" Hi, I am the first text on this file")
newfile.close()


a = open("newfile.txt") 
print(a.read())

# Delete files
""" To delete files, you need to know if it exists on any path, 
That why we need to use the os module, we then remove the file by using the
remove() function of the same os module """

import os


if os.path.exists("demofile.txt"): #Check if the file exists

    os.remove("demofile.txt") # This removes the file
else:
    print("the file does not exist")

#Delete a filder
""" use 'rmdir()' function of the os module """

import os
os.rmdir("folder_to_delete")


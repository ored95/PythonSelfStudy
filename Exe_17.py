# File. Input/Output

name = input("What is your name? ")

print("Your name is", name)

# ============ OPENING and CLOSING Files =============
# Syntax (opening_
#   file object = open(file_name [, access_mode][, buffering])
#
# Here are parameter details:
#    file_name: The file_name argument is a string value that contains the name
#                of the file that you want to access.
#    access_mode: The access_mode determines the mode in which the file has
#                to be opened, i.e., read, write, append, etc. A complete list
#                of possible values is given in the filemode table. This is optional
#                parameter and the default file access mode is read (r).
#    buffering: If the buffering value is set to 0, no buffering takes place.
#                If the buffering value is 1, line buffering is performed while
#                accessing a file. If you specify the buffering value as an integer
#                greater than 1, then buffering action is performed with the
#                indicated buffer size. If negative, the buffer size is the
#                system default (default behavior).

fo = open("temp/foo.txt", "w")

print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
print("Softspace flag : ", fo.softspace)

fo.write("Python is a great language.\nYeah its great!!\n")

fo.close()  # Close opened file

# ====== The read() method ======
# [Note] Python strings can have binary data, apart from text data.
#
# +++ Syntax:   fileObject.read([count])
#
# Here, passed parameter is the number of bytes to be read from the opened file.
# This method starts reading from the beginning of the file and if count is missing,
# then it tries to read as much as possible, maybe until the end of file.

fo = open("temp/foo.txt", "r+")

str = fo.read(10)
print("Reading string is: '", str, "'")

# Check current position
position = fo.tell();
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print("Again read String is : ", str)

# Close opened file
fo.close()

# ======= EDIT Files =======
# 1. Rename():      os.rename(current_file_name, new_file_name)
# 2. Remove():      os.remove(file_name)
# 3. mkdir():       os.mkdir("newdir")  -- make new directory
# 4. chdir():       os.chdir("newdir")  -- change current directory
# 5. getcwd():      os.getcwd()         -- display the current working directory
# 6. rmdir():       os.rmdir('dirname') -- delete the directory

import os   # Required

os.mkdir("test-dir")
print(os.getcwd())

os.chdir("test-dir")
print(os.getcwd())

fo = open("foo.txt", "w")
fo.close()

os.rename("foo.txt", "refoo.txt")
print(os.getcwd())

os.remove("refoo.txt")

os.chdir(".\..")
os.rmdir('test-dir')
print(os.getcwd())

# File/Directory methods
fo = open("temp/123", "w+")
print("File Descriptor: ", fo.fileno())
print("Connection to a tty(-like) device status:", fo.isatty())

fo.write("This is 1st line\n")
fo.write("This is 2nd line\n")
fo.write("This is 3rd line\n")
fo.write("This is 4th line\n")
fo.write("This is 5th line\n")

fo.close()

fo = open("temp/123", "w+")     # reopen working file

line = fo.readline()
print("Read line:", line)

line = fo.readline(5)
print("Read line:", line)

# Again set the pointer to the beginning
fo.seek(0, 0)

# Get the current position of the file
print("Current position:", fo.tell())

# Now truncate remaining file
print(fo.truncate())

# Try to read file now
line = fo.readline()
print("Read line:", line)

# Back to the beginning
fo.seek(0, 0)

# Read file, using the next() method
for index in range(5):
    line = fo.next()
    print("Line No", index, "-", line)

fo.close()

# The writelines() method

fo = open("temp/123", "w+")

print("Name of the file: ", fo.name)

seq = ["This is 6th line\n", "This is 7th line"]

# Write sequence of lines at the end of the file.
fo.seek(0, 2)
line = fo.writelines( seq )

# Now read complete file from beginning.
fo.seek(0,0)

for index in range(7):
    line = fo.next()
    print("Line No", index, "-", line)

fo.close()

# Remove file
os.remove("temp/123")

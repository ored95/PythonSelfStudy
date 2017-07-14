#!/usr/bin/python
# Test variables (1)
a = b = c = 1
print('\nTest #1:', a, b, c)

# Test variables (2)
a, b, c = 1, 2, "john"
print('\nTest #2:', a, b, c)

# Python has five standard data types
# + Numbers
# + String
# + List
# + Tuple
# + Dictionary

# [1. Number]
var1 = 1
var2 = 10

print('\nNumbers:', var1, var2)

del var1, var2 # delete the reference to a number object by using the del statement
print(var1, var2) (error)
# ===============================================
# Python supports four different numerical types:
#  int (signed integers)
#  long (long integers, they can also be represented in octal and hexadecimal)
#  float (floating point real values)
#  complex (complex numbers)
q = 5 - 10j
print(complex(q))


# [2. Strings]
str = 'Hello World!'
print('\nString:', str) # Prints complete string
print(str[0])           # Prints first character of the string
print(str[2:5])         # Prints characters starting from 3rd to 5th
print(str[2:])          # Prints string starting from 3rd character
print(str * 2)          # Prints string two times
print(str + "TEST")     # Prints concatenated string

# [3. Lists]
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print ('\nList:', list) # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

# [4. Tuple]
# The main differences between lists and tuples are: Lists are enclosed
# in brackets ( [ ] ) and their elements and size can be changed, while
# tuples are enclosed in parentheses ( ( ) ) and cannot be updated.
# Tuples can be thought of as READONLY lists.
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print ('\nTuple:', tuple)   # Prints complete list
print (tuple[0])            # Prints first element of the list
print (tuple[1:3])          # Prints elements starting from 2nd till 3rd
print (tuple[2:])           # Prints elements starting from 3rd element
print (tinytuple * 2)       # Prints list two times
print (tuple + tinytuple)   # Prints concatenated lists

# Attempt to update tuple, which is not allowed
tuple[2] = 1000         # Invalid syntax with tuple
list[2] = 1000          # Valid syntax with list


# [5. Dictionary]
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'Alex', 'age': 18, 'rank': 'pro'}
print('\nDictionary:', dict)    # Prints complete dictionary
print(dict['one'])              # Prints value for 'one' key
print(dict[2])                  # Prints value for 2 key
print(tinydict)                 # Prints complete dictionary
print(tinydict.keys())          # Prints all the keys
print(tinydict.values())        # Prints all the values

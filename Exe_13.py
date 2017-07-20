# Dictionary
dict = {'Name': 'Zara', 'Age': 18, 'Height': 180}
print("dict['Name']:", dict['Name'])
print("dict['Age']:", dict['Age'])

# Delete Dictionary Elements
del dict['Name']            # remove entry with key 'Name

dict.clear()                # remove all entries in dict
# print("dict['Age']: ", dict['Age'])       # Error
print(dict)
      
del dict                    # delete entire dictionary
# print("dict['Height']: ", dict['Height']) # Error

# Dictionary properties
dict = {'Name': 'Zara', 'Age': 18, 'Height': 180}
print(len(dict))    # Length of dictionary
print(str(dict))    # Print string representation of a dictionary

# type(variable)
# Returns the type of the passed variable. If passed variable is dictionary,
# then it would return a dictionary type.
print(type(dict))
print(type(dict['Age']))

# Dictionary methods

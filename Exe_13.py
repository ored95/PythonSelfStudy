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
dict.clear()
print(len(dict))

D1 = {1: 'one', 2: 'two', 3: 'three'}
D2 = D1.copy()
print(D2)

seq = ('first', 'second', 'third')
D = dict.fromkeys(seq)
print(D)

D = dict.fromkeys(seq, 10)
print(D)

D.clear()
D = {'Name': 'Zebra', 'Age': 7}
print("Age:", D.get('Age'))
print("Height:", D.get('Height', 'No given'))

# print(D.has_key('Age'))
# print(D.has_key('Height'))

# Items() returns a list of dict's (key, value) tuple pairs
print(D.items())
print(D.keys())
print(D.values())

# Setdefault() returns the key value available in the dictionary and
# if given key is not available then it will return provided default value.
print("Value:", D.setdefault('Age', None))
print("Value:", D.setdefault('Height', None))
print(D)

# Update dictionary
D1 = {'Name': 'Zebra', 'Age': 7}
D2 = {'Height': 5}
D1.update(D2)
print(D1)

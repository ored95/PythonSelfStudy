# Long string
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)
print('C:\\Python')     # Print with one '\'
print(r'C:\\Python')    # Print with two '\'

# Capitalization
src = "this is an example...!wow!!!"
print ("src.capitalize():", src.capitalize())
print ("src.center(40, '*'):", src.center(40, '*'))

# Count the appearance of substring
sub = "i"
print("src.count(sub):", src.count(sub))
print("src.count(sub, 5, 20):", src.count(sub, 5, 20))

# Decode string using the codec registered for encoding
# Example: decode(encoding='UTF-8', errors='strict')
# Here, + encoding: from Standard Encodings
#       + errors: error handling scheme, default: 'strict'
#       (other possible values: 'ignore', 'replace',
#       'xmlcharrefreplace', backslashreplace',...)
#stre = src.encode('base-64', 'strict')
#print("Encoded string:", stre)
#print("Decoded string:", stre.decode('base64', 'strict')

# Check end of string or end of string-fragment/substring
suffix = "wow!!!"
print(src.endswith(suffix))
print(src.endswith(suffix, 20))

suffix = "is"
print(src.endswith(suffix, 2, 4))
print(src.endswith(suffix, 2, 6))

# Expand tab ( '\t' )
src = "this is\tstring example!"
print("Original string:", src)
print("Default expanded tab:", src.expandtabs())
print("Double expanded tab:", src.expandtabs(16))

# Find substring position
str1 = "this is string example...!!!"
str2 = "exam"

print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 40))

# Get index of substring
print(str1.index(str2))
print(str1.index(str2, 10))
#print(str1.index(str2, 40))

# Check alphabet/number
# 1. isalnum()
# 2. isalpha()
# 3. isdigit()
print("124512509785109275".isdigit())
print(str1.isalpha())

# islower(): return TRUE if all characters are lower
print(str1.islower())

# Translate string
from string import maketrans    # Required to call maketrans funtion.

intab = "aeiou"
outtab = "12345"
transtab = maketrans(intab, outtab)

str_test = "this is string example...wow!!!"
print(str_test.translate(transtab, 'xm'))
# Answer should be: th3s 3s str3ng 21pl2....w4w!!!

# Another funtions:
# + upper(): returns a copy of the string in which all case-based characters have been uppercased
# + zfill(width): pads string on the left with zeros to fill width
# + isdecimal(): check decimal

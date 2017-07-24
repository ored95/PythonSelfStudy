# +++ The match function
# Syntax:
#    re.match(pattern, string, flags=0)
# Here,
#   + pattern: this is the regular expression to be matched.
#   + string: this is the string, which would be searched to match the pattern
#             at the beginning of string.
#   + flags: We can specify different flags using bitwise OR (|).
#
# Return
#   group(num=0): This method returns entire match (or specific subgroup num)
#   groups(): This method returns all matching subgroups in a tuple
#            (empty if there weren't any)

import re   # REQUIRED!

line = "Bob is taller than Jane"

pattern = r'(.*) is (.*?) .*'

matchObj = re.match(pattern, line, re.M|re.I)

if matchObj:
    print("matchObj.group() :", matchObj.group())
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No match!!")

# +++ The search function
searchObj = re.match(pattern, line, re.M|re.I)

if searchObj:
    print("searchObj.group() :", searchObj.group())
    print("searchObj.group(1):", searchObj.group(1))
    print("searchObj.group(2):", searchObj.group(2))
else:
    print("Nothing found!!")

# +++ Matching Versus Searching
#   Python offers two different primitive operations based on regular expressions:
# match checks for a match only at the beginning of the string, while search checks
# for a match anywhere in the string (this is what Perl does by default).

matchObj = re.match(r'Jane*', line, re.M|re.I)
if matchObj:
    print("match -> matchObj.group():", matchObj.group())
else:
    print("No match!!")

searchObj = re.search(r'Jane*', line, re.M|re.I)
if searchObj:
    print("match -> matchObj.group():", searchObj.group())
else:
    print("No match!!")

# +++ Search and Replace
#
# Syntax
#    re.sub(pattern, repl, string, max=0)
#
#    This method replaces all occurrences of the RE pattern in string with repl,
# substituting all occurrences unless max provided. This method returns modified string.

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Number : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print("Phone Number : ", num)

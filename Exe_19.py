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


# Regular-Expression Examples
"""
+++ Literal characters
python    : match "python"

+++ Character classes
[Pp]ython : match "Python" or "python"
rub[ye]   : match "ruby" or "rube"
[aeiou]   : match any lowercase vowel
[0-9]     : match any digit; same as [01233456789]
[a-z]     : match any lowercase ASCII letter
[A-Z]     : match any uppercase ASCII letter
[a-zA-Z0-9] : match any of the above
[^aeiou]  : match anything other than a lowercase vowel
[^0-9]    : match anything other than a digit

+++ Special Character Classes
.    : match any character except new line
\d   : match a digit: [0-9]
\D   : match a non-digit: [^0-9]
\s   : match a whitespace character: [\t\r\n\f]
\S   : match a non-whitespace: [^\t\r\n\f]
\w   : match a single word character: [A-Za-z0-9_]
\W   : match a non-word character: [^A-Za-z0-9_]
"""

"""
+++ Repetition cases
ruby?     : match "rub" or "ruby": the 'y' is optional
ruby*     : match "rub" plus 0 or more 'y'
ruby+     : match "rub" plus 1 or more 'y'
\d{3}     : match exactly 3 digits
\d{3,}    : match 3 or more digits
\d{3,5}   : match 3, 4 or 5 digits

+++ Nongreedy repetition
<.*>      : Greedy repetition: matches "<python>perl>"
<.*?>     : Nongreedy: matches "<python>" in "<python>perl>"

+++ Grouping with Parentheses
\D\d+     : No groups: + repeats \d
(\D\d)+   : Grouped: + repeat \D\d pair
([Pp]ython(,)?)+ : Match "Python", "Python ,python, python", etc

+++ Backreferences
([Pp]ython&\1ails   : match python&pails or Python&Pails
(['"][^\1]*\1       : Single or double-quoted string. \1 matches whatever the 1st
                      group matched. \2 matches whatever the 2nd group matched, etc

+++ Alternatives
python|perl   : match "python" or "perl"
rub(y|le)     : match "ruby" or "ruble"
Python(!+|\?) : "Python" followed by one or more ! or one ?
"""

"""
+++ Anchors (this needs to specify match position)
^Python     : match "Python" at the start of a string or internal line
Python$     : match "Python" at the end of a string or line
\APython    : match "Python" at the start of a string
Python\Z    : match "Python" at the end of a string
\bPython\b  : match "Python" at a word boundary
\brub\B     : \B is non-word boundary: match "rub" in the "rube" and "ruby" but not alone
Python(?=!) : match "Python", if followed by an exclamation point
Python(?!!) : match "Python, if not followed by an exclamation point

+++ Special Syntax with Parentheses
R(?#comment)  : match "R". All the rest is a comment
R(?i)uby      : Case-insentitive while matching "uby"
R(?i:uby)     : Same as above
rub(?:y|le))  : group only without creating \1 back reference.
"""

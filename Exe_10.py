para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)
print('C:\\Python')
print(r'C:\\Python')

src = "this is an example...!"
print ("src.capitalize():", src.capitalize())
print ("src.center(40, 'a'):", src.center(40, 'a'))

sub = "i"
print("src.count(sub):", src.count(sub))
print("src.count(sub, 5, 20):", src.count(sub, 5, 20))

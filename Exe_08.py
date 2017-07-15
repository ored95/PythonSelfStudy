# Test operator ' in '
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
if ( a in list ):
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")
if ( b not in list ):
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")

a = 2
if ( a in list ):
    print("Line 3 - a is available in the given list")
else:
    print("Line 3 - a is not available in the given list")

# Test operator ' is '

a = 20
b = 20

if ( a is b ):
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")
    
if ( id(a) == id(b) ):
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")

b = 30
if ( a is b ):
    print("Line 3 - a and b have same identity")
else:
    print("Line 3 - a and b do not have same identity")

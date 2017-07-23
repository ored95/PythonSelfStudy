# Functions/ Procedure - Python
#
# Syntax
#   def function_name( parameters ):
#       "function_docstring"
#       function_suite
#       return [expression]

def changeme(lst):
    "This changes a passed list into this function"
    lst = ['one', 'two', 3]
    print("Values inside 'changeme()' function:", lst)
    return

# Call function
lst = [1, 2, 3, 4, 5.6]
print("Given list:", lst)

changeme(lst)
print("Value after calling function:", lst)

# Keyword arguments
def printinfo( name, age ):
    "Just print information"
    print("Name:", name)
    print("Age:", age)
    return

printinfo( age = 10, name = "Julie" )

# Default Arguments
def showinfo( name, age = 18 ):
    "Just print information"
    print("Name:", name)
    print("Age:", age)
    return

showinfo( age = 10, name = "Julie" )
showinfo( name = "Jack" )

# Variable Length Arguments
#   def functionname([formal_args,] *var_args_tuple ):
#       "function_docstring"
#       function_suite
#       return [expression]

def test_argv( arg0, *vartuple ):
    "Variable passed arguments"
    print("Output is:")
    print(arg0)
    for var in vartuple:
        print(var)
    return

test_argv( 10 )
test_argv( 10, 20, 30, 40, 50 )

# The Anonymous Functions
# Syntax
#       lambda [arg1 [,arg2,.....argn]]:expression

total = lambda arg1, arg2: arg1 + arg2
print("Total:", total( 10, -5 ))


# Global vs. Local variables
s = 0   # global v.

def summer(arg1, arg2):
    s = arg1 + arg2     # local v.
    print(" Inside function, s =", s)
    return s

summer( 10, 20 )
print("Outside function, s =", s)

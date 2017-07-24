# Creating class
#
# +++ Syntax +++
# class ClassName:
#     'Optional class documentation string'
#      class_suite
#
class Employee:
    'common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee:", empCount)

    def display(self):
        print("Name:", self.name, "with Salary:", self.salary)

# Here,
#    The variable empCount is a class variable whose value is shared among all
#     instances of a this class. This can be accessed as Employee.empCount from
#     inside the class or outside the class.
#    The first method __init__() is a special method, which is called class
#     constructor or initialization method that Python calls when you create a new
#     instance of this class.
#    You declare other class methods like normal functions with the exception that
#     the first argument to each method is self. Python adds the self argument to
#     the list for you; you do not need to include it when you call the methods.
#

# Creating Instance Objects

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)

"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

# Accessing Attributes
emp1.display()
emp2.display()
print("Total Employee:", Employee.empCount)

# We can add, remove, or modify attributes of classes and objects at any time
emp1.age = 7    # Add an 'age' attribute
print(emp1.age)

emp1.age = 8    # Modify 'age' attribute
print(emp1.age)

del emp1.age    # Delete 'age' attribute

# Instead of using the normal statements to access attributes, we can use the
# following functions:
#
#    The getattr(obj, name[, default]) : to access the attribute of object.
#    The hasattr(obj,name) : to check if an attribute exists or not.
#    The setattr(obj,name,value) : to set an attribute.
#     If attribute does not exist, then it would be created.
#    The delattr(obj, name) : to delete an attribute.

print(hasattr(emp1, 'age'))     # Returns true if 'age' attribute exists
print(setattr(emp1, 'age', 8))  # Set attribute 'age' at 8
print(getattr(emp1, 'age'))     # Returns value of 'age' attribute
print(delattr(emp1, 'age'))     # Delete attribute 'age'

# +++ Built-In Class Attributes
# Every Python class keeps following built-in attributes and they can be accessed using
# dot operator like any other attribute:
#    __dict__: Dictionary containing the class's namespace.
#    __doc__: Class documentation string or none, if undefined.
#    __name__: Class name.
#    __module__: Module name in which the class is defined. This attribute is
#               "__main__" in interactive mode.
#    __bases__: A possibly empty tuple containing the base classes, in the order
#               of their occurrence in the base class list.

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

# +++ Destroying Objects (Garbage Collection)
# The __del__() destructor prints the class name of an instance that is about to be destroyed.

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "is destroyed!")

p1 = Point()
p2 = p1
p3 = p1

print("Id(P1):", id(p1))
print("Id(P2):", id(p2))
print("Id(P3):", id(p3))

del p1
del p2
del p3

# +++ Class Inheritance +++
# ---------------------------------------------------------
# Syntax
#   class SubClassName (ParentClass1[, ParentClass2, ...]):
#       'Optional class documentation string'
#       class_suite
# ---------------------------------------------------------

class Parent:       # define parent class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute:", Parent.parentAttr)

class Child(Parent):    # define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')

c = Child()         # instance of child
c.childMethod()     # child calls its method
c.parentMethod()    # calls parent's method
c.setAttr(200)      # again call parent's method
c.getAttr()         # again call parent's method

# Similar way, we can drive a class from multiple parent classes as follows:
# -----------------------------------------------
# class A:          # define class A            |
# .....                                         |
# class B:          # define class B            |
# .....                                         |
# class C(A, B):    # subclass of A and B       |
# .....                                         |
# -----------------------------------------------

# +++ Overriding Methods +++

class Parent:
    def myMethod(self):
        print("Calling parent method")

class Child(Parent):
    def myMethod(self):
        print("Calling child method")

c = Child()
c.myMethod()

# +++ Base Overloading Methods
# ===========================================================
#   Sr. No. #       Method, Description and Sample Call     #
# ===========================================================
#           #   __init__ ( self [,args...] )                #
#     1     #   Constructor (with any optional arguments)   #
#           #   Sample Call : obj = className(args)         #
# -----------------------------------------------------------
#           #   __del__( self )                             #
#     2     #   Destructor, deletes an object               #
#           #   Sample Call : del obj                       #
# -----------------------------------------------------------
#           #   __repr__( self )                            #
#     3     #   Evaluatable string representation           #
#           #   Sample Call : repr(obj)                     #
# -----------------------------------------------------------
#           #   __str__( self )                             #
#     4     #   Printable string representation             #
#           #   Sample Call : str(obj)                      #
# -----------------------------------------------------------
#           #   __cmp__ ( self, x )                         #
#     5     #   Object comparison                           #
#           #   Sample Call : cmp(obj, x)                   #
# ===========================================================

# +++ Overloading Operators: using __add__ method

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)

print(v1 + v2)

# Data Hiding
class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.__secretCount)    # Error!

# When the above code is executed, it produces the following result:
# 1
# 2
# Traceback (most recent call last):
#   File "Exe_18.py", line 225, in <module>
#     print counter.__secretCount
# AttributeError: JustCounter instance has no attribute '__secretCount'
#
# Python protects those members by internally changing the name to include the class
# name. We can access such attributes as
#        object._className__attrName
# If we would replace our last line as following, then it works for us:

print(counter._JustCounter__secretCount)    # Worked!

#Function map()
map(abs, [1, -2, -3])
#=> [1, 2, 3]

#Operator //
n = [x // 2 in for x in range(5)]
#=> [0, 0, 1, 1, 2]

n = [x // 3 in for x in range(5)]
#=> [0, 0, 0, 1, 1]

#Function list()
list() -> new empty list
list(iterable) -> new initialized list from iterable)

list(map(abs, [-1, -2, -3]) # [1, 2, 3]

#Combination
xs = [...]
ys = map(func, xs)

#Function
filter(function or none, sequence) -> list, sequence

#Example
list(filter(lambda x: x % 2 == 0), range(10)))
#=> [0, 2, 4, 6, 8]

#Function reduce()
reduce(function, sequence) -> apply a function to return a value
#For example, 
	reduce(lambda x, y: x + y, [1, 2, 3])
	#=> 6

words = ['one', 'two']
from functools import reduce
reduce (lambda a, b: a + ', ' + b, words)
#=> 'one, two'

#List comprehension
{x*x | x in Z[0, 10]}
#code:
ys = [x**2 for x in range(10)]
#=> ys = [0, 1, 4, ..]

#equivalent code:
ys = []
for x in range(10)
	ys += [x**2]
	
#map vs filter
[n for n in range(10) if n % 2 == 0]
#=> [0, 2, 4, 6, 8]

#Here, 
#	map: n for n in range(10)
#	filter: n - even
	
#Example
triple = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
[second for _, second,_ in triple]
#=> [2, 5, 8]

#Example
[a if a else 2 for a in [0, 1, 0, 3]]
#=> [2, 1, 2, 3]
 
#Example intersec(A, B)
def intersection(A, B):
	return [a for a in A for b in B if a == b]
	
#Example enum
d = {0: 'zero', 1: 'one', 2: 'two'}
{key: value for key, value in d.items() if key % 2 == 0}
#=> {0: 'zero', 2: 'two'}

@t #Decorator
def f(): ...
<=>
def f(): ...
f = t(f)

#Example
def x10(fn):
	return (lambda *args, **kwargs, fn(*args, **kwargs) * 10)
@x10

def rec(x):			#| Same as: 
	return 1/x		#|	(lambda x: (lambda(x): 1 / x) * 10)(x)
	
y = rec(2)
print(y)
#=> 5.0

#Example HTML
def paragraph(fn):
	def head(s):
		return '<h1>' + s + '</h1>'
	return head
@para

def hello_user(user_name):
	return 'Hello' + user_name + '!'
	
user_name = 'Huyen'
html = hello_user(user_name)

#//=> html:
#   	<h1>Hello Huyen!</h1>
	
#_____________Object Oriented Programming____________
#definition class:
class Point:
	pass
	
p = Point()
p.X = 1.0;
p.Y = 1.0;
p.Z = 1.0;

print(p.X, p.Y, p.Z)

class Point:
	X = 0.0
	Y = 0.0
	Z = 0.0

p = Point()
p.X = 1.0;
p.Y = 1.0;
p.Z = 1.0;

#Termination OOP
#OOP: основные концепция - понятия объекта
# 	 - обединенение полей и методов
#
#	 Объект (object) - воплощение (instance)
	
#	 Члены класса: (class members)
#		- attributes (properties)
#		- methods (изменение состояние объекта)

class Point:
	def __init__(self, x = 0, y = 0, z = 0)		#Constructor 
		self.x = x
		self.y = y
		self.z = z
		
	def SquareDistance(self, point):
		return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 + (point.z - self.z) ** 2
		
	def Distance(self, point):
		return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2 + (point.z - self.z) ** 2)
		

#Code test:
p = Point(x = 1, y = 2, z = 3)		#Call constructor 
									#Here, p -> self (1, 2, 3) -> (x, y, z)
zero = Point()						#Call init-constructor

_sqr_distance = p.SquareDistance(zero)
print (_sqr_distance)				#14

class Circle:
	def __init__(self, x, y, r):
		self.r = r
		
myCircle = Circle(1, 1, 2)			# Here, myCircle -> self, (1, 1, 5) -> (x, y, r)

#Example (blabla)
xs = [1, 2, 3]
xs.append(5)						#xs = [1, 2, 3, 5]

#Try-catch-finally
try:
	c = a / b
except ZeroDivisionError:
	c = None
	
#Example (NOTICE!!!)
class Configurable:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
	def config(self, **kwargs)
		self.__dict__.update(kwargs)
		
class Point(Configurable):
	pass

p = Point(x = 1, y = 2)
p.__dict__ => {'y': 2, 'x': 1}
p.config(x = 0, z = 3)

#result: p.x = 0, p.y = 2, p.z = 3 (add attributes)

#[Object]File OPEN:
f = open(...)
f.read()
f.write()

#sys
exit()
argv
stdout
stdin
stderr

#OS
os.path

#program.py

#!/usr/bin/cm python
..

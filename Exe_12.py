# Tuples (3 types to set a tuple
tup1 = ('physic', 'math', 'chemistry', 2, 3)
print(tup1)

tup2 = (1, 2, 3, 4, 5)
print(tup2)

tup3 = "a", "b", 'c'
print(tup3)

# Empty tuple
tup1 = ()
print(tup1)

# To write a tuple containing a single value you have to include a comma,
# even though there is only one value:
tup1 = (50,)
print(tup1)

# Accessing values in tuple
print(tup2[1], tup3[2])
print(tup2[1:5])

# Updating tuples
tup1 = 12, 34, 56.78
tup2 = ('abc', 'cde')
tup3 = tup1 + tup2
print(tup3)

# Delete tuple
del tup3
# print(tuple3)             # Error

# Tuple operations (same as list)
print(len(tup1))            # Length
print(('Hello',)*4)         # Repetitition
print(3 in (1, 2, 3))       # Membership
for x in (1, 2, 3, 4.5):    # Iteration 
    print(x)            

# Indexing
T = 1, 2, 3, 4, 5
print('T[+2]:', T[+2])
print('T[-2]:', T[-1])
print('T[1:]:', T[1:])

# Convert a list into tuple
seq = ['1', '2', 5]
T = tuple(seq)
print(T)

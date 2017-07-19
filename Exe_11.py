# Lists
list = ["math", "physic", 12, 6, ['a', 1]]
print(list[1:5])

# Update list
list[2] = ['B', 'T', 1206]
print(list)

# Append list
list.append(100)
list.append('hello')
print(list)

# Delete List Elements
# To remove a list element, you can use either the del statement if you know exactly
# which element(s) you are deleting or the remove() method if you do not know.
print("Old source:", list[5])
del list[5]
print("New source:", list[5])

# 1. Basic list operations
# ---------------------------------------------------------------------
#   Python Expression   |           Results           | Description   #
# ---------------------------------------------------------------------
#     len([1, 2, 3])    |             3               | Length        #
# [1, 2, 3] + [4, 5, 6] |      [1, 2, 3, 4, 5, 6]     | Concatenation #
#     ['Hi!'] * 4       | ['Hi!', 'Hi!', 'Hi!', 'Hi!']| Repetition    #
#     3 in [1, 2, 3]    |            True             | Membership    #
#   for x in [1, 2, 3]: |                             | Iteration     #
#       print x         |           1 2 3             |               #
# ---------------------------------------------------------------------

# 2. Indexing, Slicing, and Matrixes
# L = ['spam', 'Spam', 'SPAM!']
#
# ---------------------------------------------------------------------------
#   Python Expression   |      Results     | Description                    #
# ---------------------------------------------------------------------------
#           L[2]        |     'SPAM!'      | Offsets start at zero          #
#           L[-2]       |     'Spam'       | Negative: count from the right #
#           L[1:]       | ['Spam', 'SPAM!] | Slicing fetches sections       #
# ---------------------------------------------------------------------------

# 3. Built-in List Functions and Methods
# 3.1 Compare two lists
L1, L2 = ['a', 'b', 'c'], ['b', 'a', 'c']
print(cmp(L1, L2))

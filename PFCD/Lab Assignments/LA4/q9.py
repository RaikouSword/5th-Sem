#Given: 
address = 'B-6, Lodhi road, Delhi'
list1 = [1, 2, 3]
list2 = ['a', 1, 'z', 26, 'd', 4]
tuple1 = ('a', 'e', 'i', 'o', 'u')
tuple2 = ([2,4,6,8], [3,6,9], [4,8], 5)


# 1)
# Error: IndexError: list assignment index out of range
# list1 has only indices 0, 1, 2.

# 2)
# Executes successfully
# Output: [1, 2, 3, 1, 2, 3]

# 3)
# Error: TypeError: '<' not supported between instances of 'int' and 'str'
# list2 contains both integers and strings, so min() cannot compare them.

# 4)
# Executes successfully
# Output: 3

# 5)
# Executes successfully
# Output: ['B', '-', '6', ',', ' ', 'L', 'o', 'd', 'h', 'i', ' ', 'r', 'o', 'a', 'd', ',', ' ', 'D', 'e', 'l', 'h', 'i']

# 6)
# Executes successfully
# Output: ['a', 1, 'z', 26, 'd', 4, 'e', 5]

# 7)
# Executes successfully
# Output: ['a', 1, 'z', 26, 'd', 4, ['e', 5]]
# append() adds the whole list as a single element.

# 8)
# Executes successfully
# Output: ['gita', 'rohan', 'mohan']
# Sorted by length of each string.

# 9)
# Executes successfully
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 10)
# Executes successfully
# Output: [2]
# Deletes all elements except the first.

# 11)
# Executes successfully
# Output: [2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8]

# 12)
# Error: TypeError: 'tuple' object does not support item assignment
# Tuples are immutable.

# 13)
# Error: AttributeError: 'tuple' object has no attribute 'append'

# 14)
# Error: TypeError: can only concatenate tuple (not "int") to tuple
# Must use (5,) to make a tuple: tuple2 + (5,)

# 15)
# Executes successfully
# Output: 'a, e, i, o, u'

# 16)
# Executes successfully
# Output: [('apple', 'red'), ('orange', 'orange')]
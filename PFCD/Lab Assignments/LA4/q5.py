# a)
# Error: Invalid syntax. Variable names cannot contain spaces.
# Should be: 
# day, high_temperature, low_temperature = ('Monday', 87, 65)


# b)
# Error: IndexError: list index out of range
# Because the list has only 5 elements (indices 0–4). 
                                      

# c)
# Error: TypeError: 'str' object does not support item assignment 
# Strings in Python are immutable. 


# d)
# Error: TypeError: list indices must be integers or slices, not float


# e)
# Error:
# SyntaxError: variable name student tuple invalid (contains space).
# Even if fixed (student_tuple), the second line causes
# TypeError: 'tuple' object does not support item assignment


# f)
# Error: TypeError: can only concatenate tuple (not "str") to tuple
# If you want to concatenate, use ('Monday', 87, 65) + ('Tuesday',).


# g)
# Error: TypeError: can only concatenate str (not "tuple") to str


# h)
# Error: NameError: name 'x' is not defined
# Variable x was deleted before being printed.


# i)
# Error: ValueError: 10 is not in list
# Because 10 does not exist in the list.


# j)
# Error: TypeError: list.extend() takes exactly one argument (3 given)
# Correct form: numbers.extend([6, 7, 8])


# k)
# Error: ValueError: list.remove(x): x not in list


# l)
# Error: IndexError: pop from empty list
#Given:
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))


#Answers:
# a) Filter lambda calls: 10

# filter(lambda x: x % 2 != 0, numbers) will call the lambda function once for each element in the list to check if it satisfies the condition.    
# numbers has 10 elements, so filter’s lambda is called 10 times.



# b) Map lambda calls: 5

# map(lambda x: x ** 2, ...) is applied to the elements that passed the filter (i.e., the odd numbers).
# Odd numbers in numbers: [3, 7, 1, 9, 5] → 5 elements.
# So map’s lambda is called 5 times.



# c) Map lambda calls when reversed: 10

# If we reverse the operations:
# map(lambda x: x ** 2, numbers) is applied first. It will process all 10 elements, so map’s lambda is called 10 times.
# Then filter is applied, but the question only asks about map.
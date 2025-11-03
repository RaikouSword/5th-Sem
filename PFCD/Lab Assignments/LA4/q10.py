def sum_numeric_elements(tuple_of_tuples):
    total = 0
    for inner in tuple_of_tuples:
        for item in inner:
            if isinstance(item, (int, float)):
                total += item
    print("Sum of numeric elements:", total)

data = ((1, 2, 'a'), (3, 4, 5), ('x', 10))
sum_numeric_elements(data)

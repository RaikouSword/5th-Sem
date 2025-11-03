def sort_by_second_element(tuple_list):
    return sorted(tuple_list, key=lambda x: x[1])

data = [(1, 3), (4, 1), (2, 5), (7, 2)]
sorted_data = sort_by_second_element(data)
print("Sorted list:", sorted_data)

tuples_list = [(1, 2), (3, 4, 5), (6,), (7, 8, 9), (10, 11)]
k = int(input("Enter the length K to remove: "))

filtered_list = [t for t in tuples_list if len(t) != k]
print("Filtered list:", filtered_list)

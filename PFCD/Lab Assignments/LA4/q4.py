elements = input("Enter list elements separated by spaces: ").split()
item_to_remove = input("Enter the element you want to remove: ")
updated_list = [item for item in elements if item != item_to_remove]
print("\nOriginal List:", elements)
print("Updated List (after removing all occurrences of", item_to_remove + "):", updated_list)

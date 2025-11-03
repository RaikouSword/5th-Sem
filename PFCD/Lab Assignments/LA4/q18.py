numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
squares = [x**2 for x in numbers]
print("List of squares:", squares)

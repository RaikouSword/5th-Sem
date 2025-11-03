numbers = list(map(int, input("Enter list: ").split()))
n = numbers[0]
lst = numbers[1:]

if lst == sorted(lst):
    print("The list is already sorted")
else:
    print("The list is not sorted")

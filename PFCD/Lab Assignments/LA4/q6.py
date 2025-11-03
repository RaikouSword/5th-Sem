numbers = []

print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

search_num = int(input("Enter the number to search: "))

if search_num in numbers:
    count = numbers.count(search_num)
    print(f"{search_num} is present in the list {count} time(s).")
else:
    print(f"{search_num} is not present in the list.")

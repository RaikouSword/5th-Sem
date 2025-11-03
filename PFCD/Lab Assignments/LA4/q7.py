def cumulative_list():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    cumulative = []
    total = 0
    for num in numbers:
        total += num
        cumulative.append(total)
    return cumulative

result = cumulative_list()
print("Cumulative list:", result)

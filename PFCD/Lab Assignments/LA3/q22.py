def print_ap(first_term, common_diff, n=10):
    for i in range(n):
        term = first_term + i * common_diff
        print(term, end=' ')
    print()

a = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))
print_ap(a, d)

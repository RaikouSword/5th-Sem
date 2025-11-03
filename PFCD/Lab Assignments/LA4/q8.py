def create_multiples_lists(n):
    result = []
    for i in range(1, n + 1):
        multiples = [i * j for j in range(1, 6)]
        result.append(multiples)
    return result

n = int(input("Enter the value of n: "))
lists_of_multiples = create_multiples_lists(n)
for idx, multiples in enumerate(lists_of_multiples, start=1):
    print(f"Multiples of {idx}: {multiples}")

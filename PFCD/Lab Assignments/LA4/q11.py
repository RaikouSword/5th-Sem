M = int(input("Enter number of rows (M): "))
N = int(input("Enter number of columns (N): "))

matrix = []
for i in range(M):
    row = list(map(int, input(f"Enter {N} elements for row {i+1}, separated by spaces: ").split()))
    if len(row) != N:
        print("Error: Number of elements does not match N.")
        exit()
    matrix.append(row)

print("\nTabular format:")
for row in matrix:
    for elem in row:
        print(f"{elem}\t", end='')
    print()

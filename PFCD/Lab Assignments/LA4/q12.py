def column_sum(matrix, col_index):
    total = 0
    for row in matrix:
        total += row[col_index]
    return total

rows, cols = 3, 4
matrix = []
print("Enter a 3-by-4 matrix row by row:")
for i in range(rows):
    row = list(map(float, input().split()))
    if len(row) != cols:
        print("Error: Each row must have 4 elements.")
        exit()
    matrix.append(row)

for j in range(cols):
    print(f"Sum of column {j+1}:", column_sum(matrix, j))

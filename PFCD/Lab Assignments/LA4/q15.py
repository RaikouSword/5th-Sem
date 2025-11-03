import random

matrix = [[random.randint(0, 1) for _ in range(4)] for _ in range(4)]
for row in matrix:
    print("".join(map(str, row)))

row_index = max(range(4), key=lambda i: sum(matrix[i]))
col_index = max(range(4), key=lambda j: sum(matrix[i][j] for i in range(4)))

print("The largest row index:", row_index)
print("The largest column index:", col_index)

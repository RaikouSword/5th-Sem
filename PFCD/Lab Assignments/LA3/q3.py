def add_squares():
    total=0
    for x in range(1,51):
        if x%2==0:
            total+=x**2
    print(total)
add_squares()
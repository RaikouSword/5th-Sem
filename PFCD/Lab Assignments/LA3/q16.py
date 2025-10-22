def calc():
    n1, n2 = float(input("Num1: ")), float(input("Num2: "))
    op = input("Op (+, -, *, /): ").strip()
    if op == '+': print(n1 + n2)
    elif op == '-': print(n1 - n2)
    elif op == '*': print(n1 * n2)
    elif op == '/': print(n1 / n2 if n2 != 0 else "Error: Div by zero")
    else: print("Invalid op")

calc()

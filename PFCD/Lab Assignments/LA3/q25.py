def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(x, y):
    return gcd(x, y) == 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if are_coprime(num1, num2):
    print(f"{num1} and {num2} are coprime.")
else:
    print(f"{num1} and {num2} are NOT coprime.")

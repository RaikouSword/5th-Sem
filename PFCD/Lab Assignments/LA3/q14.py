def armstrong(num):
    digits = str(num)
    n = len(digits)
    total = sum(int(d)** n for d in digits)
    return total==num
num =int(input("Enter a number: "))
print(f"{num} is an Armstrong number ") if armstrong(num) else print(f"{num} isn't an Armstrong number")
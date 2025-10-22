def product_of_digits(num):
    product = 1
    for digit in str(abs(num)):
        product *= int(digit)
    return product

n = int(input("Enter a number: "))
print("Product of digits:", product_of_digits(n))

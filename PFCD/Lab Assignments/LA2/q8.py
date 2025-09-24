while True:
    num = int(input("Enter the number: "))
    if num>=0:
        break
print(num*2) if (num%2==0) else print(num**2)
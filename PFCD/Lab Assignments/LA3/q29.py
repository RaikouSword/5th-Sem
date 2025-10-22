def is_perfect(num):
    sum=0
    for x in range(1,num):
        if num%x==0:
            sum+=x
    return num==sum

number = int(input("Enter a number: "))
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is NOT a perfect number.")

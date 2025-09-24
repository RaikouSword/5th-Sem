num = input("Enter a number: ")
temp =0
if num.isdigit():
    temp=1
    num = int(num)

match num%5==0:
    case 1:
        print(num%5)
    case _:
        print("Invalid Input")
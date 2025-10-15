def digit(n):
    s = str(n)
    return len(s)
n = int(input())
if n>0:
    print(digit(n))
else:
    print("Invalid")
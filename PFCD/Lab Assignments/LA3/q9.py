def binary_decimal(n):
    p=num=0
    while n>0:
        num+=(n%10)*(2**p)
        p+=1
        n//=10
    return num

def decimal_binary(n):
    s = ""
    while n>0:
        s+=str(n%2)
        n//=2
    return s[::-1]

s= int(input())
print(binary_decimal(s))
n = int(input())
print(decimal_binary(n))
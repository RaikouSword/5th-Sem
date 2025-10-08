num = int(input("Enter a number: "))
sum=0
for x in range(1,num):
    if num%x==0:
        sum+=x
if num==1:
    print("Perfect")
    
else: print("Perfect") if sum==num else print("Not Perfect")
num = int(input("Enter a num: "))
sum=0 

for x in range(1, num):
    y,count= 1,0
    while y<=num:
        if x%y==0:
            count+=1
        y+=1
    if count==2:
        sum+=x

print(f"Sum of all prime numbers less than {num} is ", sum)
num = int(input("Enter a num: "))
count,freq = 0,1

while freq<=num:
    if num%freq==0:
        count+=1
    freq+=1

print(num," is a prime num") if (count==2) else print(num, " isn't a prime num")
import random 
n = random.randint(1, 10)
arr = [random.randint(1,100) for _ in range(n)]
print(arr)
print("Sum: ", sum(arr))
print("Avg: ",sum(arr)/n)
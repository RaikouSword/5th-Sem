import math

numbers = list(map(float, input("Enter ten numbers: ").split()))

mean = sum(numbers) / len(numbers)
variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
std_dev = math.sqrt(variance)

print(f"The mean is {mean:.2f}")
print(f"The standard deviation is {std_dev:.5f}")

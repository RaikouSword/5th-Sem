from collections import Counter
import statistics

ratings = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

freq = Counter(ratings)
print("Frequency of each rating:")
for rating in range(1, 6):
    print(f"{rating}: {freq[rating]}")

print("\nResponse statistics:")
print("Minimum:", min(ratings))
print("Maximum:", max(ratings))
print("Range:", max(ratings) - min(ratings))
print("Mean:", statistics.mean(ratings))
print("Median:", statistics.median(ratings))
print("Mode:", statistics.mode(ratings))
print("Variance:", statistics.variance(ratings))
print("Standard Deviation:", statistics.stdev(ratings))

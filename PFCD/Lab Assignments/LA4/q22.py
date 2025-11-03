numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

# Original: filter → map
print(list(map(lambda x: x*2, filter(lambda x: x%2==0, numbers))))
# Output: [20, 8, 4, 16, 12]

# Reversed: map → filter
print(list(filter(lambda x: x%2==0, map(lambda x: x*2, numbers))))
# Output: [20, 6, 14, 2, 18, 8, 4, 16, 10, 12]

# Explanation: Order matters; filter first reduces elements, map first doubles all, 
# making all even so filter keeps everything.

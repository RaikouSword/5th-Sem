from collections import Counter

def can_form_palindrome(s):
    char_counts = Counter(s)
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    return odd_count <= 1



def can_form_palindrome2(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    return odd_count <= 1


s = input()
print(can_form_palindrome(s))
print(can_form_palindrome2(s))
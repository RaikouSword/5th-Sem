def replace_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join('*' if ch in vowels else ch for ch in s)

text = input("Enter a string: ")
print(replace_vowels(text))

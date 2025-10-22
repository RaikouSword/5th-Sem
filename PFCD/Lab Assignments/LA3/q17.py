def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(ch for ch in s if ch not in vowels)

str = input("Enter a string: ")
print("String without vowels:", remove_vowels(str))

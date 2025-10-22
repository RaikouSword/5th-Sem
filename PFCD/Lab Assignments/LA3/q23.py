def vowel_indices(s):
    vowels = "aeiouAEIOU"
    indices = []
    for i in range(len(s)):
        if s[i] in vowels:
            indices.append(i)
    return indices

string = input("Enter a string: ")
print("Indices of vowels:", vowel_indices(string))

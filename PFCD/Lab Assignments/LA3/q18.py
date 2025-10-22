def are_anagrams(str1, str2):
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    
    return sorted(s1) == sorted(s2)

a = input("Enter first string: ")
b = input("Enter second string: ")

if are_anagrams(a, b):
    print("They are anagrams!")
else:
    print("Not anagrams.")

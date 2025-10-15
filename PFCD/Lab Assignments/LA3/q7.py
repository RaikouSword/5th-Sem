def check_vowel(s):
    s = s.lower()
    if s=='a' or s=='i' or s=='e' or s=='u' or s=='o':
        print('Its a vowel')
    else:
        print("Its a consonant")
s = input()
if len(s)==1:
    check_vowel(s)
else:
    print("Invalid")
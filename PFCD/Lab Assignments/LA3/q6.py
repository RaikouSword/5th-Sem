def palindrome(s):
    return s==s[::-1]
s = input()
if palindrome(s):
    print("Yes its a palindrome")
else:
    print("No its not a palindrome")
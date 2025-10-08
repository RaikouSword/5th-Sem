s = input()

for x in range(0,len(s)):
    res = ""
    for y in range(x,len(s)):
        res+=s[y]
        print(res)
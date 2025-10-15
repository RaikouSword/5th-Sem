import itertools

def unique_permutations(s):
    perms = itertools.permutations(s)
    unique_perms = set(''.join(p) for p in perms)
    return list(unique_perms)

s = input()
print(unique_permutations(s))



# def permute(s, b, per):
#     for i in range(len(s)):
#         if b[i]:
#             per.append(s[i])
#             b[i] = False
#             permute(s, b, per)
#             if len(per) == len(s):
#                 print("".join(per))
#             per.remove(s[i])
#             b[i] = True

# def permutate(s):
#     b = []
#     for i in s:
#         b.append(True)
#     permute(s, b, [])

# permutate("123")
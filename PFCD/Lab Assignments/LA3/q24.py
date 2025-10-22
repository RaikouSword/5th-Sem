# import string

# def remove_punctuation(s):
#     return ''.join(ch for ch in s if ch not in string.punctuation)

# text = input("Enter a string: ")
# print("Without punctuation:", remove_punctuation(text))



def remove_punctuation(s):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    return ''.join(ch for ch in s if ch not in punctuation)

text = input("Enter a string: ")
print("Without punctuation:", remove_punctuation(text))

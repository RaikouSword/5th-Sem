def shift_string(s):
    result = []
    for ch in s:
        if ch == 'z':
            result.append('a')
        else:
            result.append(chr(ord(ch) + 1))
    return ''.join(result)

input_str = input("Enter a lowercase string: ")
print(shift_string(input_str))

cols = {
    'a':1,'b':2,'c':3,'d':4,
    'e':5,'f':6,'g':7,'h':8
}
pos = input("Give input as h8,a1,etc: ")
letter = pos[0].lower()
num = pos[1:]
if letter in cols and num.isdigit():
    letter_value = cols[letter]
    num_value = int(num)
if((letter_value+num_value)%2==0):
    print('Black')
else:
    print("White")
Romans = {
    'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
}
s = input('Enter a Roman numerical: ')
total,values =0,0
for ch in reversed(s.upper()):
    value = Romans[ch]
    if value>=values:
        total+=value
    else:
        total-=value
    values = value
print(f"Integer equivalent is: {total}")
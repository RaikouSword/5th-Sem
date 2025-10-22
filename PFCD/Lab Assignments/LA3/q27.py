n = input("Enter number: ")
words = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
for d in n:
    if d.isdigit():
        print(words[int(d)], end=' ')
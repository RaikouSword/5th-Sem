from collections import Counter
arr = [1,2,3,2,3,4,4,4,5,4,5,6]
print("Mean: ",sum(arr)/len(arr))
arr.sort()
print("Median: ",arr[(len(arr)+1)//2])
maxi=0
for value in Counter(arr).values():
    if value>=maxi:
        maxi =value
print("Mode: ",maxi)
def fst(n):
    ans=[]
    while n>0:
        ans.append(n%10)
        n=n//10
    ans.sort(reverse=True)
    for x in range(0,3):
        print(ans[x],end=" ")
n = int(input())
fst(n)
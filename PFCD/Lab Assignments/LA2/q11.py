while True:
    n1,n2 = map(int,input().split())
    op = input()
    if op=='+':
        print(n1+n2)
    elif op=='-':
        print(n1-n2)
    elif op=='*':
        print(n1*n2)
    elif op=='/':
        print(n1/n2) if n2>0 else print("2nd num must not be zero")
    else:
        print("Invalid Input")
    print("Continue? (y/n)")
    if(input()=="n"):
        break
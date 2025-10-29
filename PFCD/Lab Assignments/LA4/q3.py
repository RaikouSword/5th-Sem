arr = []
while True:
    ch = input("\n1.Create 2.Show 3.Insert 4.Delete 5.Exit: ")
    if ch == '1': arr = list(map(int, input("Enter nums: ").split()))
    elif ch == '2': print(arr)
    elif ch == '3': arr.insert(int(input("Pos: ")), int(input("Val: ")))
    elif ch == '4': arr.pop(int(input("Pos: ")))
    elif ch == '5': break
    else: print("Invalid!")

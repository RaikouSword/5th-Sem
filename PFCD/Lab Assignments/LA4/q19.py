import copy

def demonstrate_copy():
    original = [['Shallow', 2, 3], [4, 5, 6]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    shallow[0][0] = 1      
    deep[0][0] = 'Deep'     

    print("Original List:", original)
    print("Shallow Copy:", shallow)
    print("Deep Copy:", deep)

demonstrate_copy()

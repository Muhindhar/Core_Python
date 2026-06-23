def union(set1, set2):
    return set1 | set2
set1 = set(map(int,input("Enter set1 values: ").split()))
set2 = set(map(int,input("Enter set2 values: ").split()))
print("Union:", union(set1, set2))
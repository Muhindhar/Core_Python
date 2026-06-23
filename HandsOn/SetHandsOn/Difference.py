def diff(set1,set2):
    return set1-set2
set1 = set(map(int, input("Enter set1 values: ").split()))
set2 = set(map(int, input("Enter set2 values: ").split()))
print("Difference :", diff(set1, set2))
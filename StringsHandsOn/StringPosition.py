string1 = input("Enter the string : ")
words = string1.title().split()
print("Print String in default order:")
print(" ".join(words))

if len(words) < 2:
    print("\nNot enough words to show positional order.")
else:
    temp = words[:]
    temp[0], temp[1] = temp[1], temp[0]
    print("\nPrint String in Positional order:")
    print(" ".join(temp))

print("\nPrint String in order of Keywords:")
print(" ".join(words[::-1]))
sentence = input("Enter any String: ")
words = sentence.split()
small=words[0]
for i in words:
    if len(i)<len(small):
        small=i
print("Smallest word:", small)
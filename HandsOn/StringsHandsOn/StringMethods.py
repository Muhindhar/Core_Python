sent = input("Enter the sentence : ")
word = input("Enter the word : ")
res = sent.rfind(word)
print(f"Last occurrence of {word} starts at index {res}")
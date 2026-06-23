word = input("Enter the sentence : ")
words = word.split()
for i in words:
    if i.isalnum() and any(ch.isdigit() for ch in i):
        print(i)
import string
sent=input("Enter the sentence with special characters :  ")
for i in string.punctuation:
    sent = sent.replace(i,"#")
print(sent)
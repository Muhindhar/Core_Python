inp = "malayalam"
stry = inp[::-1]
#if inp==inp[::-1]:
if inp.__eq__(stry):
    print("Palindrome")
else:
    print("Not a palindrome")
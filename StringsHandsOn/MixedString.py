s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s3 = ""
for i in range(len(s1)):
    s3 = s3 + s1[i] + s2[-(i+1)]

print(s3)
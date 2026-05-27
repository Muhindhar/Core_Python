
#single line
myfile = open("testfile.txt","w")
sent = input("Enter the string : ")
myfile.write(sent)
myfile.close()
print("Reading from file")
myfile = open("testfile.txt","r")
d=myfile.readlines()
for i in d:
    print(i)
myfile.close()

#multiple line
myfile = open("testfile.txt","w")
sent = input("s.no : ")
sent1 = input("name")
sent2 = input("age")
myfile.writelines([sent+"\n",sent1+"\n",sent2+"\n"])
myfile.close()
myfile = open("testfile.txt","r")
line=myfile.readlines()
for i in line:
    words = i.split()
    print(words)
myfile.close()
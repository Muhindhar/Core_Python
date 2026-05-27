myfile = open("demo.txt","r")
d=myfile.readlines()
for line in d:
    #split and splitlines
    words = line.splitlines()
    print(words)
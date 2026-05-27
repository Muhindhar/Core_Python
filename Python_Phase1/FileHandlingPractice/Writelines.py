myfile = open("demo.txt","w")
lines = ["Hello I'm Muhindhar\n", "multple lines are typing into the file\n","Hey this is muhi here!!\n"]
myfile.writelines(lines)
myfile.close()
myfile = open("demo.txt","r")
leng = myfile.readlines()
print((leng))
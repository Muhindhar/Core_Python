#write() method
myfile = open("demo.txt","w")
myfile.write("Hey i have started using files in python\n")
myfile.close()
myfile = open("demo.txt", "r")
content = myfile.read()
print(len(content))
myfile.close()


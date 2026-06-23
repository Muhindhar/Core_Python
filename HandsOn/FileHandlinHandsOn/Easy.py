def read_file(file_path):
    f=open(file_path,"r")
    print(f.read())
    f.close()
file_path=input("Enter file name: ")
read_file(file_path)

def write_to_file(file_path,msg):
    f=open(file_path,"w")
    f.write(msg)
    f.close()

    f=open(file_path,"r")
    print(f.read())
    f.close()

file_path=input("Enter file name: ")
msg=input("Enter message: ")
write_to_file(file_path,msg)

#3. append to file
def append_to_file(file_path,msg):
    f=open(file_path,"a")
    f.write("\n"+msg)
    f.close()

    f=open(file_path,"r")
    print(f.read())
    f.close()

file_path=input("Enter file name: ")
msg=input("Enter message: ")
append_to_file(file_path,msg)
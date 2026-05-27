try:
    fl = open("invalid/#demo.txt","w")
    try:
        fl.write("Writing for demo try catch")
        print("Written in file")
    finally:
        print("Final block executed")
except(IOError):
    print("Error")
else:
    print("Execute when no error occurs")
try:
    f2 = open("demo.txt","r")
    try:
        f2.read()
    except(ValueError):
        print("cannot read")
finally:
    print("Executed successfully!!")
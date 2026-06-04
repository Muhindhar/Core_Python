import re
text = "Hello this is muhi from salem tamilnadu india"
res = re.search("^H.*india*$",text)
print((res))
if(res):
    print("Matching")
else:
    print("Not matching")
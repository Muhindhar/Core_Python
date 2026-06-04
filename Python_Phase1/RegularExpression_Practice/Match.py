import re
text = "I'm muhindhar studied ece department 23497286  in kiot salem"

#match
res = re.search("ece",text)
print("matching : ",res)
print("start : ",res.start())
print("end : ",res.end())
print("span : ",res.span())
print("match : ",res.re)
print("group : ",res.group())
print("string : ",res.string)

#example

import re
pattern = r'\b\w+ing\b'
text ="walking and talking are important activities"
res = re.findall(pattern,text)
if res:
    print("match found : ",res)
else:
    print("no match")
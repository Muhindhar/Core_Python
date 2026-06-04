import re
text = "I'm muhindhar studied ece department 23497286  in kiot salem"

res = re.findall('\AI',text)
print(res)
print("-"*10)

#\S other tha  white space , \s white space alone
res = re.findall('\s',text) #\s \S
print("\S other than white space : ",res)

res = re.findall('\W',text) #\w \W
print("other than a-z0-9",res)

#res=re.finditer("m",text)
#print("iter",res)

res = re.findall("\d+",text)
print("digits as list : ",res)

#res = re.findall("End of the str : ",'\Z',text)

res = re.findall("[^a-zA-Z0-9]",text)
print("negg : ",res)

#match
res = re.search("ece",text)
print("matching : ",res)
import re
#return the word and how many times in there in the text means , same count of timers will return as list
text = "Hello athisb is muhi from salem tamilnadu india"
res=re.findall("this",text)
print(type(res))
print("result =",res)
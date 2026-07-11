inp1=tuple(input("ENter word with comma : ").split(","))
inp2=tuple(input("ENter word with comma : ").split(","))
res=()
for i in range(len(inp1)):
    res+=(inp1[i]+" "+inp2[i],)
print(res)


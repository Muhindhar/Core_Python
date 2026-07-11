class String:
    def ProcessString(self,s,a=None):
        if a is None:
            return s.upper()
        elif isinstance(a,str):
            return s[::-1]
        else:
            return len(s)

s = input("Enter a string : ")
o = String()
print(o.ProcessString(s))
print(o.ProcessString(s,"reverse"))
print(o.ProcessString(s,1))

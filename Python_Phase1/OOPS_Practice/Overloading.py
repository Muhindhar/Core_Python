class example:
    def method(self,a,b=None):
        if b is None:
            print(f"Single argument : {a}")
        elif isinstance(a,int) and isinstance(b,int):
            print(f"Two integers are given {a} and {b}")
        elif isinstance(a,str) and isinstance(b,str):
            print(f"Two strings are {a} and {b}")
        else:
            print(f"Mixed types : {a} and {b}")
            
obj = example()
obj.method("ds",33)
    
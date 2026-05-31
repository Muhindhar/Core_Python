class MYCLASS:
    def __init__(self,msg):
        self.msg = msg
        print("Init executed \n",self.msg)
    def sayhu(self):
        print("Good morning",self.msg)
    def __init__(self, name, bases):
        self.bases= bases
        print("Bases executed")
obj = MYCLASS("Morning")
obj.sayhu()



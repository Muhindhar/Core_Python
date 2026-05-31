class teammember:
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid
    def display(self):
        print(f"Team member : {self.name}, UID : {self.uid}")
class worker:
    def __init__(self, pay, pos):
        self.pay = pay
        self.pos = pos
    def display(self):
        print(f"Worker : {self.pos}, Pay : {self.pay}")
class tl(teammember, worker):
    def __init__(self, name, uid, pay, pos, exp):
        self.exp = exp
        teammember.__init__(self, name, uid)
        worker.__init__(self, pay, pos)
        print("Name : {}, Pay : {}, Position : {}, Experience : {}".format(self.name, self.pay, self.pos, self.exp))
    def show(self):
        super().display()
TL = tl("Muhindhar", 10001, 35000, "Automation tester", 5)
obj1 = worker(35000, "Tester")
obj1.display()
TL.show()
obj2 = teammember("Muhindhar", 10001)
obj2.display()
print(tl.mro())
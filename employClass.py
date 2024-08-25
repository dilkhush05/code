class employ:
    def __init__(self,role,deprt , slry):
        self.role = role
        self.deprt = deprt
        self.slry = slry

    def showdetels(self):
        print("rle is :", self.role)
        print("deprt is :", self.deprt)
        print("slry is :", self.slry)

class engineer(employ):
    def __init__(self, name, age):
        self.name =name
        self.age = age
        super().__init__("engineer","it",750000)

    def show(self):
        print("name is :",self.name)
        print("name is :",  self.age)

e1 = engineer("dilkhush thakur",19)
e1.showdetels()
e1.show()
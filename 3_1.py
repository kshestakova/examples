class Human:
    def __init__(self, name, lastname, height, age = 18):
        self.name = name
        self.lastname = lastname
        self.height = height
        self.age = age
        
    def printH(self):
        print(self.name, self.lastname, self.height, self.age )
        
alex = Human("Alex", "Ex", 187)

alex.printH()

rex = Human("Rex", "Ex", 187, 90)

rex.printH()
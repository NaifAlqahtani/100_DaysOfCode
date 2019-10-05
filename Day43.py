class identifier:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.counter = 0
    
    def printID(ID):
        ID.counter += 1
        print(f"Person {ID.counter}:\nName: {ID.name}, Age: {ID.age}")

class child(identifier):
    def __init__(self, name, age):
        identifier.__init__(self, name, age)

Naif = child("Naif", 19)

Naif.printID()
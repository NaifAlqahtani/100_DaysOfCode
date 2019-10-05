class identifier:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.counter = 0
    
    def printID(ID):
        ID.counter += 1
        print(f"Person {ID.counter}:\nName: {ID.name}, Age: {ID.age}")

Naif = identifier("Naif", 19)

Naif.printID()
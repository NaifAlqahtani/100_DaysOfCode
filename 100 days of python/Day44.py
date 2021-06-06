class identifier:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.counter = 0
    
    def printID(ID):
        ID.counter += 1
        print(f"Person {ID.counter}:\nName: {ID.name}, Age: {ID.age}")

class child(identifier):
    def __init__(self, name, age, fn):
        super().__init__(name, age)
        self.familyNumber = fn

    def familyReport(self):
        print(f"{self.name} who is {self.age} years old; has {self.familyNumber} members in his family") 

Naif = child("Naif", 19, 6)

Naif.familyReport()
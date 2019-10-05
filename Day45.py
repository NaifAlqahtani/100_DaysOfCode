class evenNumbers:
    def __iter__(self):
        self.a = 2
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            if self.a % 2 != 0:
                return x
            else:
                return '----'
        else:
            raise StopIteration

myClass = evenNumbers()
myIteration = iter(myClass)

for a in myIteration:
    print(a)
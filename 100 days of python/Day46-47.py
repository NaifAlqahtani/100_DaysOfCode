class library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf
    
    def report(obj):
        print(f"Book: {obj.book}, Shelf: {obj.shelf}")

class science_section(library):
    def __init__(self, book, shelf, name):
        super().__init__(book, shelf)
        self.bookName = name

    def finalReport(self):
        print(f"Name: {self.bookName}\nBook: {self.book}\nShelf: {self.shelf}") 

report = science_section(20, 4, "Physics Book")

report.finalReport()
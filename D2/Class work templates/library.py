import jsonHandler as IO

class Library:
    books = []

    def __init__(self, books):     
        self.books = books

    def add(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def display(self):
        pass

    def search(self):
        pass

library = Library(IO.jsonHandler.getBooks())


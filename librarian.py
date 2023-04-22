from book import Book
from libData import LibData

class Librarian:
    
    @staticmethod
    def addBook():
        title = input("Enter title of the book")
        isbn = input("Enter isbn of the book")
        authors = input("Enter authors of the book")
        available = input("Enter how many copies of the book are available")
        LibData.addBook({'title': title, 'isbn': isbn, 'authors': authors, 'available': available})

    @staticmethod
    def removeBook():
        title = input("Enter title of the book")
        authors = input("Enter authors of the book")
        LibData.removeBook({'title': title, 'authors': authors})

    @classmethod
    def menu(cls):
        while True:
            print("""
                1. Add a Book
                3. Remove a Book
                q. quit
                """)
            choice = input("select your choice: ")
            f = {
            "1": cls.addBook,
            "2": cls.removeBook,
            "q": 'q'}.get(choice,None)
            if f == 'q':
                break

            if f == None:
                print("Error, Try Again..")
            else:
                f()
from book import Book
from libData import LibData

class Memebr:
    
    def __init__(self,Id):
        self.Id = Id
    
    def borrow(self):
        isbn = input('Please enter isbn: ')
        bookId = Book.getBookIdByIsbn(isbn)
        LibData.borrowBook(self.Id, bookId)       
      
        
    
    def returnBook():
        pass
    
    def searchBook(self):
        data = input('Please enter search data: ')
        LibData.searchBook(data)
    
    def getBorrowedBook(self):
        
    
        import sqlite3       
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        
        c.execute(""" 
                  select book.isbn,book.title from book,borrow
                  where borrow.bookId = book.Id
                  and borrow.userId = :uId
                  """,{'uId':self.Id})
                  
        books = c.fetchall()
        
        if not books:
            print('You have not borrowed any book yet!')
            print('')
        else:   
            print('')
            print('*********************')
            print('* List Of Borowed Book*')
            print('*********************')
            for book in books:
                print(f"{book[0]} - {book[1]}")
            print('')
        
        conn.commit()
        conn.close()   
        
    def menu(self):
            while True:
                print("""
                  1. List Of the borrowed Books
                  2. Borrow a Book
                  3. Search
                  q. quit
                  """)
                choice = input("select your choice: ")
                f = {
                "1": self.getBorrowedBook,
                "2": self.borrow,
                "3": self.searchBook,
                "q": 'q'}.get(choice,None)
                if f == 'q':
                    break
                if f == None:
                    print("Error, Try Again..")

                else:
                    f()
    def foo(self):
        pass
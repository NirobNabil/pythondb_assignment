from book import Book
from libData import LibData
import json

    

class Member:
    
    def __init__(self,Id):
        self.Id = Id
     
    @staticmethod    
    def login(username,password):
        import sqlite3
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        c.execute(""" 
                  select Id,Name,Role from user
                  where username = :uName
                  and password = :pass
                  """,{'uName':username , 'pass':password})
        result = c.fetchone()
        
        if not result:
            return {'isExist' : False}
        else:
            return {'isExist' : True , 'id': result[0] , 'name': result[1], 
                    'role': result[2]}


    def register():
        pass
    
    @classmethod
    def load_accounts(cls):
        import sqlite3
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        c.execute("""
            DELETE FROM user;
        """)
        # c.commit()
        with open("accounts.json") as fd:
            acc = json.load(fd)
            for uid, u in acc.items():
                c.execute("""
                        INSERT INTO user
                        (id, password, name, role, fine, username)
                        VALUES(:id, :password, :name, :role, :fine, :username)
                    """,{'id':int(uid),'name':u["name"],'password':u["password"],'fine': u["fine"],'role': u['role'], 'username': u['username']})

                print(f"Saving: {u['name']}")
            
            conn.commit()


    def borrow(self):
        isbn = input('Please enter isbn: ')
        bookId = Book.getBookIdByIsbn(isbn)
        LibData.borrowBook(self.Id, bookId)    
    
    def returnBook(self):
        isbn = input('Please enter isbn: ')
        bookId = Book.getBookIdByIsbn(isbn)
        LibData.returnBook(self.Id, bookId) 
    
    def searchBook(self):
        data = input('Please enter search string: ')
        LibData.searchBook(data)
    

    def getBorrowedBook(self):
        
        import sqlite3       
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        
        c.execute(""" 
                  select books.isbn,books.title from books,borrow
                  where borrow.bookId = books.Id
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
        
        import sqlite3
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        x = c.execute('select fine from user where id=:userId', {'userId': self.Id})
        x = x.fetchone()
        previous_fine = x[0]
        print( "Notifications:" )
        print( "- You have " + str(previous_fine) + "$ outstanding fine." )

        while True:
            print("""
                1. List Of the borrowed Books
                2. Borrow a Book
                3. Return a Book
                4. Search
                q. quit
                """)
            choice = input("select your choice: ")
            f = {
            "1": self.getBorrowedBook,
            "2": self.borrow,
            "3": self.returnBook,
            "4": self.searchBook,
            "q": 'q'}.get(choice,None)
            if f == 'q':
                break
            if f == None:
                print("Error, Try Again..")

            else:
                f()
    def foo(self):
        pass


# Memebr.load_accounts()
# print(Member.login("rota", "abc"))
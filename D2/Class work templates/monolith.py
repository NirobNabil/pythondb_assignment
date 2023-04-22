import json 
import datetime
import uuid

class jsonHandler:
    bookFile = "BOOK.json"
    userFile = "login.json"

    @classmethod
    def getBooks(cls):
        with open(cls.bookFile, "r") as fd:
            books = json.load(fd)
        
        dBooks = {}
        
        for b in books:
            if b["isbn"] in dBooks:
                dBooks[str(b['isbn'])].append(Book(b["title"], b["authors"], str(b["isbn"]), b["publisher"]))
            else:
                dBooks[str(b['isbn'])] = [Book(b["title"], b["authors"], str(b["isbn"]), b["publisher"])]
        
        return dBooks
    
    @classmethod
    def getUsers(cls):
        with open(cls.userFile, "r") as fd:
            acc = json.load(fd)

        users = {}

        for uid, u in acc.items():
            if u["uType"] == "Student":
                pass
            else:
                users[uid] = Staff( uid, u["name"], u["dept"])

        return users

    def saveBooks():
        pass

    def saveUsers():
        pass


class Book: 
    reserved_by = None
    borrowed_by = None
    borrow_date = None
    def __init__(self, title, authors, isbn, publisher):
        self.title = title
        self.author = authors
        self.isbn = isbn
        self.publication = publisher

    def __repr__(self):
        return f"""
            isbn: {self.isbn}
            title: {self.title}
            authors: {self.author}
        """
    
    def showduedate(self):
        print( self.borrow_date + datetime.datetime.timedelta(days=7) )

    def reservationstatus(self):
        if( self.resrved_by == None ):
            print("Not reserved")
            return
        
        user_id = self.resrved_by

        print("Reserved by ", libmanSystem.users[user_id])
        
    def feedback(self):
        pass
    def bookrequest(self):
        pass
    def renewinfo(self):
        pass


class Library:
    books = []

    def __init__(self, books):
        self.books = books

    def add(self, book):
        if( book.isbn not in self.books ):
            self.books[book.isbn] = []
        self.books[book.isbn].append(book)

    def delete(self, isbn):
        del self.books[isbn]

    def update(self, isbn, book):
        self.books[isbn] = book

    def display(self, isbn):
        print(self.books[isbn])

    def display_all(self):
        print(self.books)

    def search(self):

        def by_author():
            searchString = input("Enter author name")
            for k, b in self.books.items():
                # print(type(b), b)
                if searchString in b[0].author:
                    print(b)

        def by_title():
            searchString = input("Enter title")
            for k, b in self.books.items():
                if searchString in b[0].title:
                    print(b)

        print("""
        Search by:
            1. title
            2. author
        """)
        choice = input("select your choice: ")
        f = {
            "1": by_title,
            "2": by_author,
        }.get(choice,None)

        if f == None:
            print("Error, Try Again..")
        else:
            f()
        


class Account:
    def __init__(self, id, user_id):
        self.id = id
        self.user_id = user_id
        self.no_borrowed_books = 0
        self.no_reserved_books = 0
        self.no_returned_books = 0
        self.no_lost_books = 0
        self.fine_amount = 0

    def calculate_fine(self):
        return self.fine_amount

class User:
    def __init__(self, id, name):
        self.account_id = None
        self.name = name
        self.id = id

    def __repr__(self):
        return f"{self.name}"

    def verify(self):
        pass

    def check_account(self):
        print("Associated account id: ", self.account_id)

    def get_book_info(self):
        account = libmanSystem.accounts[self.account_id]
        print("Number of books borrowed: ", account.no_borrowed_books)
        print("Number of books returned: ", account.no_returned_books)
        print("Number of books reserved: ", account.no_reserved_books)
        print("Number of books lost: ", account.no_lost_books)

    def search(self):
        LibManSystem.library.search()

    def reserve(self):
        isbn = input("Enter isbn of the book you want to reserve: ")
        account = libmanSystem.accounts[self.account_id]
        for book in LibManSystem.library.books[isbn]:
            if book.reserved_by == None:
                book.reserved_by = self.account_id
                account.no_reserved_books = account.no_reserved_books + 1
                print("Reserved")
                return
            
        print("reservation slot full")
        return

    def borrow(self):

        account = libmanSystem.accounts[self.account_id] 

        if( account.no_borrowed_books >= 5 ):
            print("you have reached maximum number of borrowed books!")
            return

        isbn = input("Enter isbn of the book you want to borrow: ")
        account.no_borrowed_books = account.no_borrowed_books + 1

        book = None
        for b in libmanSystem.library.books[isbn]:
            if ( b.borrowed_by == None and ( b.reserved_by == None or b.reserved_by == self.account_id ) ):
                book = b
                break

        if( book == None ):
            print("Book not available!")
            return

        book.borrowed_by = account.id
        book.borrow_date = datetime.datetime.today()
        print("Borrowed succesfully")
    

    def renew(self):
        isbn = input("Enter isbn of the book you want to renew: ")
        account = libmanSystem.accounts[self.account_id] 

        book = None
        for b in libmanSystem.library.books[isbn]:
            if ( b.borrowed_by == account.id ):
                book = b

        if book == None:
            print("invalid request")
            return
        
        book.borrow_date = datetime.datetime.today()
        print("renewed succesfully")

    def pay_fine(self):
        account = libmanSystem.accounts[self.account_id]
        print("You have ", account.calculate_fine(), " amount due in fine")
        amount = input("Enter amount of fine you are paying: ")
        account.fine_amount = account.fine_amount - int(amount)
        print("Transaction succesful")

      
    def return_book(self):
        isbn = input("Enter isbn of the book you want to return: ")
        account = libmanSystem.accounts[self.account_id]

        for book in libmanSystem.library.books[isbn]:
            if book.borrowed_by == self.account_id:
                if( datetime.datetime.today() - book.borrow_date > datetime.timedelta(days=7) ):
                    account.fine_amount = account.fine_amount + 100

                account.no_borrowed_books = account.no_borrowed_books - 1
                account.no_returned_books = account.no_returned_books + 1 
                book.borrowed_by = None
                book.borrow_date = None
                print("Returned succesfully")
                return
        
        print("Error processing request")



class Student(User):
    def __init__(self, uid, name, sClass):
        super().__init__(uid, name)
        self.Class = sClass
    
    def menu(self):
        while True:
            print("""
              1. search
              2. borrow
              3. return
              4. get book info
              5. check_account
              6. reserve
              7. renew
              8. pay fine
              9. logout
              """)
            choice = input("select your choice: ")
            f = {
                "1": self.search,
                "2": self.borrow,
                "3": self.return_book,
                "4": self.get_book_info,
                "5": self.check_account,
                "6": self.reserve,
                "7": self.renew,
                "8": self.pay_fine,
                "9": libmanSystem.menu}.get(choice,None)
            
            if f == None:
                print("Error, Try Again..")
            else:
                f()




class Staff(User):
    def __init__(self, uid, name, sDept):
        super().__init__(uid, name)
        self.Dept = sDept
    
    def menu(self):
        while True:
            print("""
              1. search
              2. borrow
              3. return
              4. get book info
              5. check_account
              6. reserve
              7. renew
              8. pay fine
              9. logout
              """)
            choice = input("select your choice: ")
            f = {
                "1": self.search,
                "2": self.borrow,
                "3": self.return_book,
                "4": self.get_book_info,
                "5": self.check_account,
                "6": self.reserve,
                "7": self.renew,
                "8": self.pay_fine,
                "9": libmanSystem.menu}.get(choice,None)
            
            if f == None:
                print("Error, Try Again..")
            else:
                f()



class Librarian():
    def __init__(self, name, password):
        self.id = uuid.uuid4()
        self.name = name
        self.password = password    
    
    def verify_librarian(self, name, password):
        if self.name == name and self.password == password:
            return True
        else:
            return True
        
    def display_book_detailed_info(self):
        isbn = input("Enter isbn of the book you want to look for: ")
        for book in libmanSystem.library.books[isbn]:
            print(book)
            print("     Borrowed by: ", book.borrowed_by)
            if book.borrowed_by != None:
                print("     Borrowed by: ", book.borrow_date)
            print("     reserved by: ", book.reserved_by)



    def menu(self):
        while True:
            print("""
              1. add book
              2. remove book(s)
              3. update book
              4. display book by isbn
              5. search
              6. display all books
              7. display detailed book info
              8. logout
              """)
            choice = input("select your choice: ")
            f = {
                "1": libmanSystem.library.add,
                "2": libmanSystem.library.delete,
                "3": libmanSystem.library.update,
                "4": libmanSystem.library.display,
                "5": libmanSystem.library.search,
                "6": libmanSystem.library.display_all,
                "7": self.display_book_detailed_info,
                "8": libmanSystem.menu}.get(choice,None)
            
            if f == None:
                print("Error, Try Again..")
            else:
                f()



class LibManSystem:
    
    def __init__(self):
        self.library = Library(jsonHandler.getBooks())
        self.users = jsonHandler.getUsers()
        self.accounts = []

        for uid, u in self.users.items():
            self.accounts.append(Account(len(self.accounts)-1, uid))
            u.account_id = len(self.accounts)-2

    def menu(self):
        while True:
            print("""
                1. register
                2. login 
                """)
            choice = input("select your choice: ")

            f = {
                "1": self.register,
                "2": self.login}.get(choice,None)
            
            if f == None:
                print("Error try again!")
            else:
                f()


    def register(self):
        print("""
              1. as student
              2. as staff 
              3. as librarian
              """)
        choice = input("select your choice: ")
        
        uid = uuid.uuid4()
        name = input("Enter name: ")
        if choice == "1":
            Class = input("Enter class: ")
            self.users.append( Student( uid, name, Class) )
        elif choice == "2":
            Dept = input("Enter Department: ")
            self.users.append( Staff( uid, name, Dept ) )
        elif choice == "3":
            password = input( "Enter password: " )
            self.librarian = Librarian( name, password ) 

    def login(self):
        print("""
              1. as student
              2. as staff 
              3. as librarian
              """)
        choice = input("select your choice: ")
        
        name = input("Enter name: ")
        if choice == "1" or choice == "2":
            for uid, u in self.users.items():
                if u.name == name:
                    u.menu()      

        elif choice == "3":
            password = input( "Enter password: " )
            if self.librarian.name == name and self.librarian.password == password:
                self.librarian.menu() 
            


libmanSystem = LibManSystem()

libmanSystem.menu()



    
# library.add(Book("tt","aa","456","me"))

# users["007"].menu()

# print(users["007"].borrow())
# print(users["007"].return_book())


# print(library.books["076790818X"].borrowed_by)



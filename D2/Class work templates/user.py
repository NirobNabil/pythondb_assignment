import library as lb
import jsonHandler

class User:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def gg(self):
        print(lb.library.books)

    def __repr__(self):
        return f"{self.name}"

    def verify(self):
        pass

    def check_account(self):
        pass

    def get_book_info(self):
        pass



class Staff(User):
    def __init__(self,name,uid, sDept):
        super().__init__(name, uid)
        self.Dept = sDept
    
    def menu(self):
        while True:
            print("""
              1. option-1s
              2. option-2s
              3. option-3
              q. quit
              """)
            choice = input("select your choice: ")
            f = {
            "1": self.borrow,
            "2": self.foo,
            "3": self.foo,
            "q": self.foo}.get(choice,None)
            if f == None:
                print("Error, Try Again..")
            else:
                f()

    def borrow(self):
        isbn = input("Enter isbn of the book you want to borrow")
        # print(LibDatabase.dBooks)
        pass


users = jsonHandler.handler.getUsers()

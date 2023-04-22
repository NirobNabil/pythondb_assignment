# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:05:50 2023

@author: id003941
"""
import json 
class LibManSystem:
    
    def __init__(self):
        LibManSystem.loadBooks()
       
        LibManSystem.login()
        
    
    @staticmethod
    def loadBooks():
        with open("BOOK.json", "r") as fd:
            books = json.load(fd)
        for b in books:
            # print(b['isbn'], b['title'])
            LibDatabase.dBooks[b['isbn']] = Book(b["title"],
                                                 b["authors"],
                                                 b["isbn"])
    @classmethod                                            
    def authenticate(cls,uid,pswd):
        with open("login.json", "r") as fd:
            acc = json.load(fd)
            # print(acc)  
        if uid in acc:
            if acc[uid]['pswd'] == pswd:
                return True, acc[uid]
        return False, None
    
    @classmethod       
    def login(cls):
        print("Welcome to BCU Lib System")
        uid = input("Enter uid: ")
        pswd = input("Enter your password: ")
        v, u =LibManSystem.authenticate(uid, pswd)
        if v:
            print("Welcome....")
            if u["uType"] == "Staff":
                usr = Staff(u["name"],uid,u["dept"])
                usr.menu()
            elif u["uType"] == "student":
                pass
            elif u["uType"] == "librarian":
                pass
            else:
                print("Data error")
                

        else:
            print("Login failure")
            
            
    def reg():
        pass
    def logout():
        pass
    
#%%
class Book:
    def __init__(self,title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
      
        
    def __repr__(self):
        return f"""
    {self.title}
    {self.author}
    """
    def showduedate(self):
        pass
    def reservationstatus(self):
        pass
    def feedback(self):
        pass
    def bookrequest(self):
        pass
    def renewinfo(self):
        pass

    
#%%
class LibDatabase:
    dBooks = {}
    def __init__(self):
        pass
    
#%%
class User:
    def __init__(self,name, uid,):
        self.name = name
        self.uid = uid
        
    def __repr__(self):
        return f"{self.name}"
    
class Student(User):
    def __init__(self,name,uid, sclass):
        super().__init__(name, uid)
        self.sclass = sclass
    
    
            
            
        
class Staff(User):
    def __init__(self,name,uid, sDept):
        super().__init__(name, uid)
        self.sDept = sDept
    
    def foo(self):
        print("fooo....")
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
            "1": self.foo,
            "2": self.foo,
            "3": self.foo,
            "q": self.foo}.get(choice,None)
            if f == None:
                print("Error, Try Again..")
            else:
                f()
        
    pass
class Librarian(User):
    def __init__(self,name,lid,password,searchstring):
        self.name = name
        self.lid = lid
        self.password = password
        self.searchstring = searchstring
        
    def __repr__(self):
        pass
    def varifylibrarian(self):
        pass
    def search(self):
        pass        
#%%
bcu =  LibManSystem()
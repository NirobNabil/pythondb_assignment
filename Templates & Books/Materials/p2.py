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
        with open("data.json", "r") as fd:
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
        v, u = LibManSystem.authenticate(uid, pswd)
        if v:
            print("Welcome....")
            if u["uType"] == "Staff":
                usr = Staff(u["name"],uid,u["dept"])
                usr.menu()
            elif u["uType"] == "Student":
                usr = Student(u["name"],uid,u["class"])
                usr.menu()
            elif u["uType"] == "Libarian":
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
    def __init__(self, title, author, isbn):
      self.title = title
      self.author = author
      self.isbn = isbn
    
    def __repr__(self):
        return f"""
{self.title}
    ~ {self.author}
    """
    


#%%
class LibDatabase:
    dBooks = {}
    def __init__(self):
        pass
    
#%%
class User:
    def __init__(self,name, uid):
        self.name = name
        self.uid = uid

        
    def __repr__(self):
        return f"{self.name}"
    
class Student(User):
    def __init__(self, name, uid, sClass):
        super().__init__(name, uid)
        self.sClass = sClass
   
    def foo(self):
        print("You called foo")
        
    def menu(self):
        while True:
            print("""
                  1. option-1
                  2. option-2
                  3. option-3
                  q. Quit
                  
                  """) 
            choice = input("Please select your option: ")
            f = {"1": self.foo,
                 "2": self.foo,
                 "3": self.foo,
                 "q": None}.get(choice,None)
            if choice == "q" or choice =="Q":
                break
            elif f == None:
                print("Try again...")
            else:
                f()
                
        
class Staff(User):
    def __init__(self, name, uid, sDept):
        super().__init__(name, uid)
        self.sDept = sDept

    def menu(self):
        print("""
              1. option-1s
              2. option-2s
              3. option-3
              q. Quit
              
              """)         
class Libarian(User):
    pass
        
#%%
bcu =  LibManSystem()
from book import Book
from libData import LibData
import uuid

import sqlite3 

conn = sqlite3.connect("mydb.db", detect_types=sqlite3.PARSE_DECLTYPES |
                                                        sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()


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


    @staticmethod
    def printUsers():
        g = cursor.execute("SELECT * from user")
        print("id\t\tname\t\trole\t\tfine\t\tusername")
        for u in g.fetchall():
            print(u[0], "\t\t", u[1], "\t\t", u[3], "\t\t", u[4], "\t\t", u[5])

    @staticmethod
    def updateUser():
        
        def name():
            name = input("Enter new name: ")
            cursor.execute("update user set name=:name where username=:username", {
                'name': name,
                'username': username 
            })

        def password():
            password = input("Enter new pass: ")
            cursor.execute("update user set password=:password where username=:username", {
                'password': password,
                'username': username 
            })

        def role():
            role = input("Enter new role: ")
            cursor.execute("update user set role=:role where username=:username", {
                'role': role,
                'username': username 
            })


        username = input("enter username: ")
        print("""
                1. update name
                2. update password
                3. update role
                q. quit
                """)
        choice = input("select your choice: ")
        f = {
            "1": name,
            "2": password,
            "3": role,
            "q": 'q'
        }.get(choice,None)
        if f == 'q':
            return
        else:
            f()
        

        conn.commit()


    @staticmethod
    def register():
        uid = uuid.uuid4()
        name = input("Enter name: ")
        password = input("Enter password: ")
        role = input("Enter role: ")
        username = input("Enter username: ")
        
        cursor.execute("""
            INSERT INTO user
            (password, name, role, fine, username)
            VALUES(:password, :name, :role, :fine, :username)
        """,{'name':name,'password':password,'fine': 0,'role': role, 'username': username})
        conn.commit()

        print("User created succesfully")



    @classmethod
    def menu(cls):
        while True:
            print("""
                1. Add a Book
                2. Remove a Book
                3. Print all users
                4. update user
                5. register new user
                q. quit
                """)
            choice = input("select your choice: ")
            f = {
                "1": cls.addBook,
                "2": cls.removeBook,
                "3": cls.printUsers,
                "4": cls.updateUser,
                "5": cls.register,
                "q": 'q'}.get(choice,None)
            if f == 'q':
                break

            if f == None:
                print("Error, Try Again..")
            else:
                f()
import sqlite3 

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

from book import Book
from member import Member
from librarian import Librarian


while True:

    print("----------------------- LOGIN -------------------------")
    username = input("Enter username: ")
    password = input("Enter password: ")

    loginDict = Member.login(username, password)
    if loginDict['isExist'] == False:
        print('Invalid Credentials!')
        continue

    if loginDict['role'] == 'librarian':
        Librarian.menu()
    else:
        member = Member(loginDict['id'])    
        member.menu() 


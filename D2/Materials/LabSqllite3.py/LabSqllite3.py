#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:36:30 2023

@author: Stish
"""


#%%
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS  books(
    isbn integer PRIMARY KEY,
    title text,
    author text,
    available integer 
    )""")
#%%
class Book:
    def __init__(self,isbn,title,author,available=3):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = available

    def __repr__(self): 
        return f"{self.title}, {self.author}"
    

def insertBook(b):    
    with conn:
        c.execute("INSERT INTO books VALUES(:isbn,:title,:author,:available)",{'isbn':b.isbn,'title':b.title,'author':b.author,'available':b.available})

def search(opt,s):
    s = '%'+s+'%'
    cmd = f'SELECT * FROM books WHERE {opt} LIKE :s'
    if opt in ['title','author']:
       # c.execute('SELECT * FROM books WHERE title LIKE :s', {'s':s})
        c.execute(cmd, {'s':s})
        # c.execute('SELECT * FROM books WHERE title =:s', {'s':s})
    else: 
        c.execute('SELECT * FROM books WHERE author LIKE :s', {'s':s})
        # c.execute('SELECT * FROM books WHERE author =:s', {'s':s})
    return c.fetchall()    
    
    return c.fetchall()
def getBooks():
    with conn:
        c.execute('SELECT * FROM books')
    return c.fetchall()
def issue_book(b):
    with conn:
        c.execute("""UPDATE books SET issued=:issued)",
                  WHERE title=:title AND 'author':author""",
                  {'title':b.title, 'author':b.author, 'available':b.available})
                  
def return_book(b):
    with conn:
        c.execute("""UPDATE books SET issued=:issued)",
                  WHERE title=:title AND 'author':author""",
                  {'title':b.title, 'author':b.author, 'available':b.available})
                  
def remove_book(b):
    with conn:
        c.execute("""DELETE from books WHERE title=:title AND author=:author""",
                  {'title':b.title, 'author':b.author})
        


#%%
import json

def loadBooks(cls):
    with open('book2.json') as fd:
        books= json.load(fd)
        for b in books:
            nb= Book(b['isbn'],b["title"],b["authors"])
            insertBook(nb)
#%%
print(getBooks())


#%%                  
b1 = Book(1,"Harry Potter and the Half-Blood Prince (Harry Potter  #6)",
          "Douglas Adams")

b2= Book(2,"The Ultimate Hitchhiker's Guide: Five Complete Novels and One Story (Hitchhiker's Guide to the Galaxy  #1-5)",
          "J.K. Rowling/Mary GrandPré")
b3 = Book(3,"Life at BCU", "Stish Sarna")
b4 = Book(321,"Python Programming", "Stish Sarna")
b5 = Book(123,"Data Structures", "Stish Sarna")
#%%
insertBook(b1)
insertBook(b3)
insertBook(b4)
insertBook(b5)
#%%
print('>>', search('author',"Stish"))
print('remove')
remove_book(b4)
print('>>', search('author',"Stish"))
#%%
# 

class Student:
    def __init__(self,f,s,age, course):
        self.f = f
        self.s = s
        self.age= age
        self.course = course
        
    def __repr__(self):
        return f"{self.f} - {self.course}"
    
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("""CREATE TABLE student(
    first text,
    second text,
    age integer,
    course text
    )""")
# NULL, INTEGER, REAL, TEXT, BLOB

conn.commit()
conn.close()
#%%
conn = sqlite3.connect('test.db')
c=conn.cursor()
c.execute("INSERT INTO student VALUES('Stish','sarna',21,'programming21')")
c.execute("INSERT INTO student VALUES('rita','sarna',22,'programming22')")
c.execute("INSERT INTO student VALUES('kieran','sarna',23,'programming23')")
c.execute("INSERT INTO student VALUES('veni','sarna',24,'programming24')")
c.execute("INSERT INTO student VALUES('shiv','sarna',25,'programming25')")
conn.commit()
conn.close()

#%%
conn = sqlite3.connect('test.db')
c=conn.cursor()
c.execute("SELECT * FROM student WHERE second ='sarna'")
# print(c.fetchone())
# print(c.fetchmany(5))
print(c.fetchall()) # returns in a list
conn.commit()
conn.close()

#%%
s = Student('STISH',"SARNA",888,'PYTHON')
s2 = Student('RITA',"SARNA",786,'c#')
conn = sqlite3.connect('test.db')
c=conn.cursor()

#option-1
c.execute("INSERT INTO student VALUES(?,?,?,?)",(s.f,s.s,s.age,s.course))
conn.commit()

#option-2 better
c.execute("INSERT INTO student VALUES(:f,:s,:age,:course)",
          {'f':s2.f,'s':s2.s,'age':s2.age,'course':s2.course})
conn.commit()
c.execute("SELECT * FROM student WHERE second ='SARNA'")
print(c.fetchall()) # returns in a list

conn.close()

#%%
conn = sqlite3.connect('test.db')
c=conn.cursor()
# c.execute("SELECT * FROM student WHERE second =?",('sarna',))
c.execute("SELECT * FROM student WHERE second =:last",{'last':'SARNA'})
# print(c.fetchone())
# print(c.fetchmany(5))
print(c.fetchall()) # returns in a list
conn.commit()
conn.close()

#%%
# import sqlite3

# conn = sqlite3.connect('mysqlite.db')
# c = conn.cursor()
# 			
# #get the count of tables with the name
# c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='students1' ''')

# #if the count is 1, then table exists
# if c.fetchone()[0]==1 : 
# 	print('Table exists.')
# else :
# 	print('Table does not exist.')
# 			
# #commit the changes to db			
# conn.commit()
# #close the connection
# conn.close()

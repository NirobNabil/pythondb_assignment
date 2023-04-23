from book import Book
import datetime
import time

import sqlite3 

conn = sqlite3.connect("mydb.db", detect_types=sqlite3.PARSE_DECLTYPES |
                                                        sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()

class LibData:
    
    @staticmethod
    def borrowBook(userId,bookId):

        ava = Book.checkAvailbality(bookId)
        if ava > 0 :
            cursor.execute("""
                      insert into borrow(userId,bookId,date)
                      values(:uid,:bid,:date)              
                      """,{'uid':userId, 'bid':bookId, 'date': datetime.datetime.now()})
            conn.commit()
            # conn.close()                      
            Book.updateAvailibility(ava-1,bookId)
            print('Book is borrowed by you\n')

        else:
            print('The book is not available\n')

    @staticmethod
    def returnBook(userId, bookId):

        x = cursor.execute( 'select date from borrow where userId=:uid and bookId=:bid', {'uid':userId, 'bid':bookId})
        x = x.fetchone()


        time_difference = datetime.datetime.now() - x[0]
        if( time_difference.days >= 0 ):
            x = cursor.execute('select fine from user where id=:userId', {'userId': userId})
            x = x.fetchone()
            previous_fine = x[0]

            print("previous fine: ", previous_fine)
            cursor.execute('''
                update user
                set fine = :newFine
                where id = :userId
            ''', { 'userId': userId, 'newFine': previous_fine + 100})

        cursor.execute('''
            delete from borrow where userId=:uid and bookId=:bid
        ''', {'uid':userId, 'bid':bookId})
        conn.commit()

        # cursor.execute("""
        #             delete from borrow where userId=:uid and bookId=:bid
        #         """,{'uid':userId, 'bid':bookId})
        # conn.commit()
        # # conn.close()                      
        # Book.updateAvailibility(ava-1,bookId)
        print('Book is returned by you\n')

            
    @staticmethod
    def searchBook(data):
        import sqlite3
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        data = '%'+data+'%'
        c.execute(""" 
                  select title,authors,isbn from books
                  where title like :d
                  or authors like :d
                  or ISBN like :d                  
                  """,{'d':data})
        result = c.fetchall() 
        print('ISBN - Title - Authors')
        i = 1
        for book in result:
            print(f"{i} - {book[2]} - {book[0]} - {book[1]}")
            i = i +1
        conn.commit()
        conn.close() 


    @staticmethod
    def addBook(data):
        b = Book(data)
        Book.addBook(b)

    @staticmethod
    def removeBook(data):
        b = Book(data)
        Book.remove_book(b)

    


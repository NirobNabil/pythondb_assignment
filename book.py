import json

import sqlite3
conn = sqlite3.connect("mydb.db")
c = conn.cursor()

class Book:

    def __init__(self, book):
        print(book)
        self.title = book['title'] if 'title' in book else None
        self.isbn = book['isbn'] if 'isbn' in book else None
        self.authors = book['authors'] if 'authors' in book else None
        self.available = book['available'] if 'available' in book else None

    @classmethod  
    def loadBooks(cls):
        import sqlite3
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        c.execute('''
            DELETE FROM books;
        ''')
        with open('book2.json') as fd:
            books= json.load(fd)
            print(books)
            for b in books:
                c.execute('''
                    INSERT INTO books 
                    (id, isbn, title, authors, available)
                    VALUES(:id, :isbn,:title,:authors,:available)
                ''',{'id': b["bookID"], 'isbn':b["isbn"],'title':b["title"],'authors':b["authors"],'available':1})

                print(f"Saving: {b['isbn']}")
            
            conn.commit()
    
    # def search(opt,s):
    #     s = '%'+s+'%'
    #     cmd = f'SELECT * FROM books WHERE {opt} LIKE :s'
    #     c.execute(cmd, {'s':s})

    #     return c.fetchall()    
        
    def getBooks():
        c.execute('SELECT * FROM books')
        return c.fetchall()
    
    # def issue_book(b):
    #     c.execute('''
    #             UPDATE books SET issued=:issued)",
    #             WHERE title=:title AND 'author':author
    #         ''', {'title':b.title, 'author':b.author, 'available':b.available})
                    
    def return_book(b):
        c.execute('''UPDATE books SET available=:available)",
                WHERE title=:title AND 'authors' LIKE :authors''',
                {'title':b.title, 'authors':b.authors, 'available':b.available})
        conn.commit()

    def remove_book(b):
        c.execute('''DELETE from books WHERE title=:title AND authors LIKE :authors''',
                {'title':b.title, 'authors':b.authors})
        conn.commit()
            
          
    def addBook(b):
        c.execute('''
                INSERT INTO books (isbn, title, authors, available) VALUES(:isbn,:title,:authors,:available)
            ''', {'isbn':b.isbn,'title':b.title,'authors':b.authors,'available':b.available})
        conn.commit()
      
    
    def deleteBook(b):
        c.execute('''
                DELETE FROM books WHERE title=:title AND authors LIKE :authors
            ''', {'title':b.title, 'authors':b.authors})
    

    def checkAvailbality(bookId):
        import sqlite3
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        c.execute('''
                  select available from books
                  where id = :bid          
                  ''',{'bid':bookId})

        ava = c.fetchone()[0]
        conn.close()
        return ava
    
    def updateAvailibility(number, bookId):
        import sqlite3
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        c.execute(''' 
                      update books set
                      available = :nava
                      where id = :bid
                      ''' , {'nava' : number, 'bid':bookId})
        
        conn.commit()
        conn.close()
    
    @staticmethod
    def getBookIdByIsbn(isbn):
        import sqlite3
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        c.execute('''
                  select id from books
                  where isbn = :is          
                  ''',{'is':isbn})
        result = c.fetchone()
        
        conn.commit()
        conn.close()
        return result[0]
    

# Book.loadBooks()
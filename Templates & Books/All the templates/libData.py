from book import Book
class LibData:
    
    @staticmethod
    def borrowBook(userId,bookId):
        import sqlite3       
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        ava = Book.checkAvailbality(bookId)
        if ava > 0 :
            c.execute("""
                      insert into borrow(userId,bookId)
                      values(:uid,:bid)              
                      """,{'uid':userId, 'bid':bookId})
            conn.commit()
            conn.close()                      
            Book.updateAvailibility(ava-1,bookId)
            print('Book is borrowed by you')

        else:
            print('The book is not available')
            
    @staticmethod
    def searchBook(data):
        import sqlite3       
        conn = sqlite3.connect("mydb.db")
        c = conn.cursor()
        data = '%'+data+'%'
        c.execute(""" 
                  select title,authors,isbn from book
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

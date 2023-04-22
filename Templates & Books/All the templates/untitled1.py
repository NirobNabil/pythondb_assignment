import json
import sqlite3


conn = sqlite3.connect("mydb.db")
c = conn.cursor()


with open("books.json", encoding="utf-8" ) as fd:
    books = json.load(fd)
 
for book in books:    
    c.execute("""INSERT INTO book(isbn,title,authors,available)
                  VALUES(:is,:ti,:au,:av)""",{'is':book['isbn'], 'ti': book['title'], 'au' : book['authors'], 'av': 3})


conn.commit()
conn.close()



#%%
# Create Borrowing function
import sqlite3
from book 

userId = 1
bookId = 25

conn = sqlite3.connect("mydb.db")
c = conn.cursor()




if ava > 0 :
    c.execute("""
              insert into borrow(userId,bookId)
              values(:uid,:bid)              
              """,{'uid':userId, 'bid':bookId})
    c.execute(""" 
              update book set
              available = :nava
              where id = :bid
              """ , {'nava' : ava-1, 'bid':bookId})
else:
    print('The book is not available')

conn.commit()
conn.close()

#%%


userId = 1
bookId = 19



import sqlite3


conn = sqlite3.connect("mydb.db")
c = conn.cursor()


c.execute(""" 
          select available from book
          where id = :bId          
          """,{'bId':bookId})


available = c.fetchone()[0]

if available > 0 :
    c.execute("""
              Insert into borrow(bookId,userId)
              Values(:bId,:uId)
              """,{'bId':bookId,'uId':userId})
              
    new_available =  available - 1           
    c.execute("""update book set
              available = :ava
              where id = :bid
                      """,{'ava':new_available,'bid' : bookId})

else :
    print('Sorry! this book is not available')    


conn.commit()
conn.close()


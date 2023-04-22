import sqlite3

conn = sqlite3.connect("mydb.db")

c = conn.cursor()



c.execute("""
          Select * from book
          """)


books = c.fetchall()
print(books)

conn.commit()
conn.close()


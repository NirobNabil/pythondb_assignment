import sqlite3 

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# conn.execute('''
#     DROP TABLE user;
# ''')


conn.execute('''
    CREATE TABLE user (
        id             INTEGER PRIMARY KEY   AUTOINCREMENT,
        name           TEXT    NOT NULL,
        password       TEXT    NOT NULL,
        role           TEXT    NOT NULL,
        fine           INTEGER     NOT NULL,
        username       TEXT        NOT NULL
    );
''')



# conn.execute('''
#     DROP TABLE books;
# ''')

conn.execute('''
    CREATE TABLE books (
        id             INTEGER  PRIMARY KEY  AUTOINCREMENT,
        title          TEXT    NOT NULL,
        isbn           TEXT    NOT NULL,
        authors        TEXT    NOT NULL,
        available      INTEGER     NOT NULL
    );
''')


conn.execute('''
    CREATE TABLE borrow (
        userId INTEGER NOT NULL,
        bookId INTEGER NOT NULL,
        date timestamp,
        FOREIGN KEY(userId) REFERENCES user(ID),
        FOREIGN KEY(bookId) REFERENCES book(ID)
    );
''')
    

conn.commit()
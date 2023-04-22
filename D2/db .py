import sqlite3
import json 

conn = sqlite3.connect('test.db')
c = conn.cursor()

# conn.execute('''
#     DROP TABLE user;
# ''')

conn.execute('''
    CREATE TABLE user
    (
        id INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL
        password text not null,
    );

    create table borrow 
    (
        id int primary key not null,
        user_id int fore
        book_id  
    )
''')

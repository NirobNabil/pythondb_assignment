import sqlite3
import json 

conn = sqlite3.connect('test.db')
c = conn.cursor()

# conn.execute('''
#     DROP TABLE user;
# ''')

# conn.execute('''
#     CREATE TABLE user
#     (ID INT PRIMARY KEY     NOT NULL,
#     NAME           TEXT    NOT NULL);
# ''')


# with open("login.json", "r") as fd:
#     acc = json.load(fd)

#     for uid, u in acc.items():
#         conn.execute("INSERT INTO user VALUES (?, ?);", (uid, u["name"]))

# conn.commit()

# res = conn.execute("SELECT * FROM user;")

# print(res.fetchall())

# conn.close()

c = conn.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='user';''')

# print(c.fetchone())

if c.fetchone()[0] == 'user':
    print("found")
else:
    print("noit")



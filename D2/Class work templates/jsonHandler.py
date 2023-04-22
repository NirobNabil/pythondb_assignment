import json
import book
import user

class jsonHandler:
    bookFile = "BOOK.json"
    userFile = "login.json"

    @classmethod
    def getBooks(cls):
        with open(cls.bookFile, "r") as fd:
            books = json.load(fd)
        
        dBooks = {}
        
        for b in books:
            # print(b['isbn'], b['title'])
            dBooks[b['isbn']] = book.Book(b["title"], b["authors"], b["isbn"], b["publisher"])
        
        return dBooks
    
    @classmethod
    def getUsers(cls):
        with open(cls.userFile, "r") as fd:
            acc = json.load(fd)

        users = {}

        for uid, u in acc.items():
            if u["uType"] == "Student":
                pass
            else:
                users[uid] = user.Staff( uid, u["name"])

        return users

    def saveBooks():
        pass

    def saveUsers():
        pass

handler = jsonHandler()
    
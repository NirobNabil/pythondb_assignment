
class Book:
    def __init__(self, title, authors, isbn, publisher):
        self.title = title
        self.author = authors
        self.isbn = isbn
        self.publication = publisher

    def __repr__(self):
        return f"""
            {self.title}
            {self.author}
        """
    
    def showduedate(self):
        pass
    def reservationstatus(self):
        pass
    def feedback(self):
        pass
    def bookrequest(self):
        pass
    def renewinfo(self):
        pass
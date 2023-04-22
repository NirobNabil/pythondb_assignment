
class Account:
    def __init__(self, user_id):
        self.user_id = user_id
        self.no_borrowed_books = True
        self.no_reserved_books = True
        self.no_returned_books = True
        self.no_lost_books = True
        self.fine_amount = 0

    def calculate_fine(self):
        pass
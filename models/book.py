class Book:

    book_count = 0

    def __init__(self, title, author, member, due_date="", genre="", reviews=None):
        self.title = title
        self.author = author
        self.member = member
        self.due_date = due_date
        self.genre = genre
        self.reviews = reviews or []
        Book.book_count += 1

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

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not value or not value.strip():
            raise ValueError("Book author cannot be empty.")
        self._author = value.strip()

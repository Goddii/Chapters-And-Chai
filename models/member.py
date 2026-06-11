class Member:
    """A library member who can own many books."""

    member_count = 0

    def __init__(self, name, email, books=None):
        self.name = name
        self.email = email
        self.books = books or []
        Member.member_count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Member name cannot be empty.")
        self._name = value.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value or "@" not in value:
            raise ValueError("Member email must contain @.")
        self._email = value.strip()

    def add_book(self, book_title):
        """Add a book title to this member if it is not already listed."""
        if book_title not in self.books:
            self.books.append(book_title)

    def to_dict(self):
        """Convert a Member object into a dictionary for JSON saving."""
        return {
            "name": self.name,
            "email": self.email,
            "books": self.books,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Member object from data loaded from JSON."""
        return cls(
            data["name"],
            data["email"],
            data.get("books", []),
        )

    def __str__(self):
        return f"{self.name} ({self.email}) - {len(self.books)} book(s)"
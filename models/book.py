from models.review import Review

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

    def add_review(self, review):
        self.reviews.append(review)

    def complete_for_member(self, member_name):
        """Mark a member's review as finished, or create one if needed."""
        for review in self.reviews:
            if review.assigned_to == member_name:
                review.mark_finished()
                return review

        review = Review(5, "Completed book.", "finished", member_name)
        self.add_review(review)
        return review

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "member": self.member,
            "due_date": self.due_date,
            "genre": self.genre,
            "reviews": [review.to_dict() for review in self.reviews],
        }
    
    @classmethod
    def from_dict(cls, data):
        reviews = [Review.from_dict(review) for review in data.get("reviews", [])]
        return cls(
            data["title"],
            data["author"],
            data["member"],
            data.get("due_date", ""),
            data.get("genre", ""),
            reviews,
        )

    def __str__(self):
        due_text = f", due {self.due_date}" if self.due_date else ""
        genre_text = f", {self.genre}" if self.genre else ""
        return f"{self.title} by {self.author} ({self.member}{genre_text}{due_text})"
class Review:
    """A review for a book, assigned to a member."""

    allowed_statuses = ["reading", "finished", "dropped"]

    def __init__(self, rating, notes, status="reading", assigned_to=""):
        self.rating = rating
        self.notes = notes
        self.status = status
        self.assigned_to = assigned_to
 @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        value = int(value)
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5.")
        self._rating = value
 @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in self.allowed_statuses:
            raise ValueError("Status must be reading, finished, or dropped.")
        self._status = value
 def mark_finished(self):
        """Mark this review/book as finished."""
        self.status = "finished"
def to_dict(self):
        """Convert a Review object into a dictionary for JSON saving."""
        return {
            "rating": self.rating,
            "notes": self.notes,
            "status": self.status,
            "assigned_to": self.assigned_to,
        }

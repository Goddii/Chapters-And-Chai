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

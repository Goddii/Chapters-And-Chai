class Review:
    """A review for a book, assigned to a member."""

    allowed_statuses = ["reading", "finished", "dropped"]

    def __init__(self, rating, notes, status="reading", assigned_to=""):
        self.rating = rating
        self.notes = notes
        self.status = status
        self.assigned_to = assigned_to

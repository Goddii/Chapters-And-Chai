import pytest

from models.book import Book

def test_book_can_have_many_reviews():
    book = Book("Dune", "Herbert", "John")
    book.add_review(Review(5, "Amazing", "finished", "John"))
    book.add_review(Review(4, "Good", "reading", "Sara"))

    assert len(book.reviews) == 2
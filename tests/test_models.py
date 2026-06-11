import pytest

from models.book import Book

def test_book_can_have_many_reviews():
    book = Book("Dune", "Herbert", "John")
    book.add_review(Review(5, "Amazing", "finished", "John"))
    book.add_review(Review(4, "Good", "reading", "Sara"))

    assert len(book.reviews) == 2

def test_complete_book_marks_member_review_finished():
    book = Book("Dune", "Herbert", "John")
    book.add_review(Review(4, "Still reading", "reading", "John"))

    book.complete_for_member("John")

    assert book.reviews[0].status == "finished"
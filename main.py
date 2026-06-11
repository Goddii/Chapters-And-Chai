import argpase


from lib.functions import add_book, add_member, add_review, complete_book 
from lib.functions import list_books, list_members, list_reviews, setup_files
from models.review import Review


def buid_parser():
    # create all cli commands and arguments
    parser= argparse.ArgumentParser(description="Chapters & Chai CLI")
    subparsers = parser.add_parsers(dest="command", required=True)

    add_member_parser = subparsers.add_parser("add-member", help="Add a member")
    add_member_parser.add_argument("--name", required=True)
    add_member_parser.add_argument("--email", required=True)
    add_member_parser.set_defaults(func=add_member)


    list_members_parser = subparsers.add_parser("list-members", help="List members")

    add_book_parser = subparser.add_parser("add-book", help='Add a book')
    add_book_parser.add_argument("--member", required=True)
    add_book_parser.add_argument("--title", required=True)add_book_parser.add_argument("--author", required=True)add_book_parser.add_argument("--due-date", required=True)
    add_book_parser.add_argument("--genre", default="")
    add_book_parser.set_defaults(func=add_book)

    list_book_parser = subparser.add_parser("list-books", help="List books")
    list_books_parser.add_argument("--member", default="")
    list_books_parser.set_defaults(func=list_books)

    add_review_parser = subparsers.add_parser('add-review', help="Add a review")
    add_review_parser.add_argument("--book", required=True)
    add_review_parser.add_argument("--rating", required=True, type=int)
    add_review_parser.add_argument("--notes", default='')
    add_review_parser.add_argument("--status", default="reading", choices=Review.allow_statuses)
    add_review_parser.add_argument("--assigned-to", required=True)
    add_review_parser.add_argument("--member", required=True)
    add_review_parser.set_defaults(func=add_reviews)

    list_reviews_parser = subparsers.add_parser("list-reviews", help="List reviews for a book")
    list_reviews_parser.add_argument("--book", required=True)
    list_reviews_parser.add_argument("--member", default="")
    list_reviews_parser.set_defaults(func=list_reviews)

    complete_book_parser = subparsers.add_parser("complete-book", help="Mark a book as finished")
    complete_book_parser.add_argument("--book", required=True)
    complete_book_parser.add_argument("--member", required=True)
    complete_book_parser.set_defaults(func=complete_book)
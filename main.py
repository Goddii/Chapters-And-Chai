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


    list_member
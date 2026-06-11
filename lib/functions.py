from datetime import date, timedelta
import json
import pathlib import Path

from dateutils import parser as date_parser
from rich.console import Console
from rich.table import Table

from models.book import Book
from models.member import Member
from models.review import Review

DATA_DIR = Path("data")
MEMBER_FILE = DATA_DIR / "members.json"
BOOK_FILE = DATA_DIR / "books.json"


def save_json(file_path, data):
    """ save data to a json file"""
    DATA_DIR.mkdir(exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def load_json(file_path):
    """ load json data.if file is missing or broken return an empty"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def setup_files():
    """create starter data files if they do not exist"""
    DATA_DIR.mkdir(exist_ok=True)
    if not MEMBERS_FILE.exists():
        save_json(MEMBERS_FILE, [])
    if not BOOK_FILE.exists():
        save_json(BOOK_FILE, [])

def load_members():
    """ load saved members"""
    return [Member.from_dict(item) for item in load_json(MEMBERS_FILE)]




def load_book():
    # load saved books
    return [Book.from_dict(item) for item in load_json(BOOKS_FILE)]     

def save_book(books):
    # save book objects
    save_json(BOOK_FILE, [book.to_dict() for book in books]) 

def find_book(books,title, member_name=''):
    # find a book by title with optional member filter
    for book in books:
        same_title = book.title.lower() == title.lower()
        same_member = not member_name or book.lower() == member_name.lower()
        if same_title and same_member:
            return book
    return None  

def add_book(args):
    # cli action to add a book for a member
    pass                    










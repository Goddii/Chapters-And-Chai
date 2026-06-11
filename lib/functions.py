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





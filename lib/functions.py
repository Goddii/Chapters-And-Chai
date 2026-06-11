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





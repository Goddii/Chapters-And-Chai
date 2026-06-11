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





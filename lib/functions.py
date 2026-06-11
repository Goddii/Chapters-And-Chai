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

def save_members(members):
    """ save member object """
    save_json(MEMBERS_FILE, [member.to_dict() for member in member])


def load_book():
    # load saved books
    return [Book.from_dict(item) for item in load_json(BOOKS_FILE)]     

def save_books(books):
    # save book objects
    save_json(BOOK_FILE, [book.to_dict() for book in books]) 

def find_member(members, name):
    """ find member by name """
    for member in members:
        if member.lower() == members.lower():
            return member
    return None

              

def find_book(books,title, member_name=''):
    # find a book by title with optional member filter
    for book in books:
        same_title = book.title.lower() == title.lower()
        same_member = not member_name or book.lower() == member_name.lower()
        if same_title and same_member:
            return book
    return None  

def format_due_date(text):
    """ format simple date words or normal dates"""
    if not text:
        return ''

    text = text.lower().strip()
    today = date.today()

    if text == "today":
        return today.isoformat()

    if text == "tomorrow":
        return (today + timedelta(days=1).isoformat())
    if text.startswith("next"):
        weekdays =["monday", "tuesday","wednesday","thursday","friday","saturday","sunday"]
        if day_name in weekdays:
            days_ahead = weekdays.index(day_name) - today.weeday()
            if days_ahead <= 0:
                days_ahead += 7
            return (today + timedelta(days=days_ahead)).isoformat()

    return date_parser.parse(text).date().isoformat()               

def add_member(args):
    """cli to add members"""
    members = load_members()
    if find_member(members, args.name):
        console.print(f'[red]Member already exists:[/red] {args.name}')
        return
    member = Member(args.name, args.email)
    members.append(member)
    save_members(members)
    console.print(f"[green]Added member:[/green] {member}")

 def list_members(args):
    """CLI action: list members."""
    table = Table(title="Members")
    table.add_column("Name")
    table.add_column("Email")
    table.add_column("Books")

    for member in load_members():
        table.add_row(member.name, member.email, str(len(member.books)))

    console.print(table)       
def add_book(args):
    """CLI action: add a book for a member."""
    members = load_members()
    books = load_books()
    member = find_member(members, args.member)

    if not member:
        console.print(f"[red]Member not found:[/red] {args.member}")
        return
    if find_book(books, args.title, args.member):
        console.print(f"[red]Book already exists:[/red] {args.title}")
        return

    try:
        due_date = format_due_date(args.due_date)
    except ValueError:
        console.print("[red]Could not understand that due date.[/red]")
        return

    book = Book(args.title, args.author, member.name, due_date, args.genre)
    books.append(book)
    member.add_book(book.title)
    save_books(books)
    save_members(members)
    console.print(f"[green]Added book:[/green] {book}")


def list_books(args):
    """CLI action: list books."""
    books = load_books()
    if args.member:
        books = [book for book in books if book.member.lower() == args.member.lower()]

    table = Table(title="Books")
    for heading in ["Title", "Author", "Member", "Genre", "Due Date", "Reviews"]:
        table.add_column(heading)

    for book in books:
        table.add_row(
            book.title,
            book.author,
            book.member,
            book.genre or "-",
            book.due_date or "-",
            str(len(book.reviews)),
        )

    console.print(table)                  

def add_review(args):
    """CLI action: add a review to a book."""
    members = load_members()
    books = load_books()
    book = find_book(books, args.book, args.member)

    if not book:
        console.print(f"[red]Book not found:[/red] {args.book}")
        return

    assigned_to = args.assigned_to or args.member or book.member
    if not find_member(members, assigned_to):
        console.print(f"[red]Assigned member not found:[/red] {assigned_to}")
        return

    try:
        review = Review(args.rating, args.notes, args.status, assigned_to)
    except ValueError as error:
        console.print(f"[red]{error}[/red]")
        return

    book.add_review(review)
    save_books(books)
    console.print(f"[green]Added review for {book.title}:[/green] {review}")

   def list_reviews(args):
    """CLI action: list reviews for one book."""
    book = find_book(load_books(), args.book, args.member)
    if not book:
        console.print(f"[red]Book not found:[/red] {args.book}")
        return

    table = Table(title=f"Reviews for {book.title}")
    for heading in ["Rating", "Status", "Assigned To", "Notes"]:
        table.add_column(heading)

    for review in book.reviews:
        table.add_row(str(review.rating), review.status, review.assigned_to, review.notes)

    console.print(table) 


def complete_book(args):
    """CLI action: mark a book as finished for a member."""
    members = load_members()
    books = load_books()

    if not find_member(members, args.member):
        console.print(f"[red]Member not found:[/red] {args.member}")
        return

    book = find_book(books, args.book, args.member)
    if not book:
        console.print(f"[red]Book not found for {args.member}:[/red] {args.book}")
        return

    book.complete_for_member(args.member)
    save_books(books)
    console.print(f"[green]Completed book:[/green] {book.title} for {args.member}")





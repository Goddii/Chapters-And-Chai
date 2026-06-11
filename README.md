# Chapters & Chai 📚

A command-line library tracker that lets members log books they are reading, add reviews, and track reading progress — all stored locally as JSON files.

---

## Table of Contents

- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Class Relationships](#class-relationships)
- [Installation](#installation)
- [Usage](#usage)
  - [Members](#members)
  - [Books](#books)
  - [Reviews](#reviews)
- [Command Reference](#command-reference)
- [Data Storage](#data-storage)

---

## Project Structure

```
chapters-and-chai/
├── main.py                  # Entry point — CLI argument parsing and routing
├── requirements.txt         # Project dependencies
├── models/
│   ├── member.py            # Member class
│   ├── book.py              # Book class
│   └── review.py            # Review class
├── lib/
│   └── functions.py         # All CLI actions, load/save logic, helper utilities
└── data/                    # Auto-created on first run
    ├── members.json          # Persisted member records
    └── books.json            # Persisted book records (reviews nested inside)
```

---

## How It Works

`main.py` is the entry point. It uses `argparse` to define all CLI subcommands and routes each one to its matching function in `lib/functions.py`.

`functions.py` is where all the logic lives. Every action follows the same pattern:

```
load data from JSON → find/validate objects → mutate → save back to JSON
```

The three model classes (`Member`, `Book`, `Review`) are pure data containers. They define validation rules via `@property` setters and handle serialization with `to_dict()` / `from_dict()` methods. They do no file I/O themselves.

---

## Class Relationships

```
Member  ──(one-to-many)──▶  Book  ──(one-to-many)──▶  Review
```

- One **Member** can have many **Books**
- One **Book** can have many **Reviews**
- Each **Review** has an `assigned_to` field pointing back to a member by name
- The `Member → Book` link is stored as a name string on the Book (`book.member = "Alice"`), not a live object reference

> **Note:** Reviews are not stored in a separate file. They are nested inside each book's record in `books.json`.

---

## Installation

**Prerequisites:** Python 3.8+

**1. Clone the repository**

```bash
git clone <your-repo-url>
cd chapters-and-chai
```

**2. Install dependencies**

Using pipenv (recommended):
```bash
pipenv install
pipenv shell
```

Or using pip:
```bash
pip install -r requirements.txt
```

**3. Verify setup**

```bash
python3 main.py --help
```

The `data/` directory and JSON files are created automatically on first run.

---

## Usage

### Members

**Add a new member**
```bash
python3 main.py add-member --name "Alice" --email "alice@email.com"
```

**List all members**
```bash
python3 main.py list-members
```

---

### Books

**Add a book for a member**
```bash
python3 main.py add-book \
  --member "Alice" \
  --title "Atomic Habits" \
  --author "James Clear" \
  --due-date "2025-07-01" \
  --genre "Self Help"
```

The `--due-date` flag accepts natural language as well as standard dates:

| Input | Resolves to |
|---|---|
| `"today"` | Current date |
| `"tomorrow"` | Next day |
| `"next monday"` | Coming Monday |
| `"2025-07-01"` | July 1, 2025 |

**List all books**
```bash
python3 main.py list-books
```

**List books for a specific member**
```bash
python3 main.py list-books --member "Alice"
```

**Mark a book as finished**
```bash
python3 main.py complete-book --book "Atomic Habits" --member "Alice"
```

If the member has no review yet for that book, one is automatically created with a default rating of 5 and status `finished`.

---

### Reviews

**Add a review to a book**
```bash
python3 main.py add-review \
  --book "Atomic Habits" \
  --member "Alice" \
  --assigned-to "Alice" \
  --rating 4 \
  --notes "Really practical read" \
  --status "finished"
```

| Flag | Required | Details |
|---|---|---|
| `--book` | Yes | Title of the book |
| `--member` | Yes | Member who owns the book |
| `--assigned-to` | Yes | Member the review is assigned to |
| `--rating` | Yes | Integer from 1 to 5 |
| `--notes` | No | Free-text notes (defaults to empty) |
| `--status` | No | `reading`, `finished`, or `dropped` (defaults to `reading`) |

**List all reviews for a book**
```bash
python3 main.py list-reviews --book "Atomic Habits"
```

**List reviews for a book filtered by member**
```bash
python3 main.py list-reviews --book "Atomic Habits" --member "Alice"
```

---

## Command Reference

| Command | Required flags | Optional flags |
|---|---|---|
| `add-member` | `--name` `--email` | — |
| `list-members` | — | — |
| `add-book` | `--member` `--title` `--author` `--due-date` `--genre` | — |
| `list-books` | — | `--member` |
| `complete-book` | `--book` `--member` | — |
| `add-review` | `--book` `--member` `--assigned-to` `--rating` | `--notes` `--status` |
| `list-reviews` | `--book` | `--member` |

---

## Data Storage

All data is stored in the `data/` directory as JSON files. The files are created automatically if they do not exist.

**`data/members.json`** — stores member records:
```json
[
  {
    "name": "Alice",
    "email": "alice@email.com",
    "books": ["Atomic Habits"]
  }
]
```

**`data/books.json`** — stores book records with reviews nested inside:
```json
[
  {
    "title": "Atomic Habits",
    "author": "James Clear",
    "member": "Alice",
    "due_date": "2025-07-01",
    "genre": "Self Help",
    "reviews": [
      {
        "rating": 4,
        "notes": "Really practical read",
        "status": "finished",
        "assigned_to": "Alice"
      }
    ]
  }
]
```

> The `Member → Book` link is a name string. If a member's name is changed directly in the JSON, book ownership links will break. Always use the CLI to manage data.

---

## Dependencies

| Package | Purpose |
|---|---|
| `rich` | Pretty terminal tables and colored output |
| `python-dateutil` | Flexible due date parsing |
| `pytest` | Running tests |

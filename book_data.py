# book_data.py - Handles saving and loading books from file

def load_books():
    """Loads books from the file into a list"""
    try:
        with open("books.txt", "r") as file:
            books = [line.strip().split(" | ") for line in file.readlines()]
        return books
    except FileNotFoundError:
        return []

def save_books(books):
    """Saves book list to the file"""
    with open("books.txt", "w") as file:
        for book in books:
            file.write(" | ".join(book) + "\n")

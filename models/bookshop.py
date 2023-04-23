from models.book import *

book1 = Book("LOTR", "Bilbo Baggins", "Fantasy", True)
book2 = Book("Star Wars", "Darth Vader", "Space", False)
book3 = Book("Harry Potter", "Dumbledore", "Wizards", False)
book4 = Book("Cooking", "Gordon Ramsy", "Kitchen", True)
book5 = Book("Walking Hills", "Brian", "Hiking", True)
book6 = Book("Scot History", "William", "Haggis", True)

booklist = [book1, book2, book3, book4, book5, book6]

def add_new_book(book):
    booklist.append(book)

def remove_book(book):
    book_to_remove = None
    for book in booklist:
        if book == book:
            book_to_remove = book
            break
    booklist.remove(book_to_remove)
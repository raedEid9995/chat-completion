class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        self.is_available = True

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book.title)
            print(f"{self.name} has borrowed {book.title}.")
        else:
            print(f"{book.title} is currently unavailable.")

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)
            print(f"{self.name} has returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"{member.name} is now a member of the library.")

    def list_available_books(self):
        available_books = [book.title for book in self.books if book.is_available]
        print("Available books:", ", ".join(available_books))

# Example usage
library = Library()

# Adding books
book1 = Book("1984", "George Orwell")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book(book1)
library.add_book(book2)

# Registering a member
john = Member("John Doe")
library.register_member(john)

# Borrowing and returning books
john.borrow_book(book1)
john.borrow_book(book2)
john.return_book(book1)

# Listing available books
library.list_available_books()

from abc import ABC, abstractmethod
from logger import logging


class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
    

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None: pass

    @abstractmethod
    def remove_book(self, title: str) -> None: pass

    @abstractmethod
    def get_books(self) -> list[Book]: pass

class Library(LibraryInterface):
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title:str) -> None:
        self.books = [book for book in self.books if book.title != title]
        

    def get_books(self) -> list[Book]:
       return self.books

class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logging.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logging.info(f"Book removed: {title}")

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logging.info("No books in the library.")
        else:
            for book in books:
                logging.info(str(book))

def main():
    library = Library()
    library_manager = LibraryManager(library)
    
    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()
        
        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            library_manager.add_book(title, author, year)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            library_manager.remove_book(title)
        elif command == "show":
            library_manager.show_books()
        elif command == "exit":
            break
        else:
            logging.info("Invalid command. Please try again.")

if __name__ == "__main__":
    main()


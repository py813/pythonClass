#OOP CHALLENGE

#Define Book Class
class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity
        
    def __str__(self):
        return f"{self.title}, {self.author}, {self.isbn}, {self.genre}, {self.quantity}"  
        
#Define Author Class
class Author:
    def __init__(self, name, bDate, nationality):
        self.name = name
        self.bDate = bDate
        self.nationality = nationality
        
    def __str__(self):
        return f"{self.name}, {self.bDate}, {self.nationality}"  
        
#Define Catalog class
class LibraryCatalog:
    
    def __init__(self, LibraryTable = []):
       self.LibraryTable = LibraryTable
    
    def add_book(self, title, author, isbn, genre, quantity):
        newTitle = title
        newTitle = Book(title, author, isbn, genre, quantity)
        self.LibraryTable.append(newTitle)


    def search_books_by_author(self, author):
        for book in self.LibraryTable:
            if book.author == author:
                print(f"{book.title} {book.author} {book.isbn}, Genre - {book.genre}, Quantity - {book.quantity}")
        
    def search_books_by_genre(self, genre):
        for book in self.LibraryTable:
            if book.genre == genre:
                print(f"{book.title} {book.author} {book.isbn}, Genre - {book.genre}, Quantity - {book.quantity}")
        print()
        
    def display_all_books(self):
        for book in self.LibraryTable:
            print(f"{book.title} {book.author} {book.isbn}, Genre - {book.genre}, Quantity - {book.quantity}")
        print()

    def remove_book(self, isbn):
        for book in self.LibraryTable:
            if book.isbn == isbn:
                self.LibraryTable.remove(book)
                break



# Sample interaction in a program
library_catalog = LibraryCatalog()

# Adding books to the catalog
library_catalog.add_book("Introduction to Python", Author("John Smith", "1980-01-15", "USA"), "978-0-13-467094-2", "Programming", 5)
library_catalog.add_book("The Art of Fiction", Author("Jane Doe", "1975-06-22", "UK"), "978-0-14-144160-4", "Fiction", 3)
library_catalog.add_book("Science and Nature", Author("David Brown", "1990-03-10", "Canada"), "978-1-23-456789-0", "Science", 7)

# Displaying all books
library_catalog.display_all_books()

# Searching for books
library_catalog.search_books_by_author("John Smith")
library_catalog.search_books_by_genre("Science")

# Removing a book
library_catalog.remove_book("978-0-13-467094-2")

# Displaying updated catalog
library_catalog.display_all_books()
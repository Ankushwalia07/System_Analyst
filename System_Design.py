''' System Design and Architecture. For this advanced Python code example,
let's build a simple library management system. The application will allow
 users to add, search, and manage books in a library. We'll use Object-Oriented
 Programming (OOP) principles to design the system and implement it.'''
import uuid

class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.book_id = str(uuid.uuid4())  # Generate a unique ID for each book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        return found_books

    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        return found_books

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book removed successfully!")
                return
        print("Book not found!")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search by Title")
        print("3. Search by Author")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author name: ")
            genre = input("Enter the book genre: ")
            isbn = input("Enter the book ISBN: ")

            new_book = Book(title, author, genre, isbn)
            library.add_book(new_book)

        elif choice == "2":
            title = input("Enter the book title to search: ")
            found_books = library.search_by_title(title)
            if found_books:
                print("Matching books found:")
                for book in found_books:
                    print(f"{book.title} by {book.author}")
            else:
                print("No matching books found!")

        elif choice == "3":
            author = input("Enter the author name to search: ")
            found_books = library.search_by_author(author)
            if found_books:
                print("Books by the author found:")
                for book in found_books:
                    print(f"{book.title} by {book.author}")
            else:
                print("No books by the author found!")

        elif choice == "4":
            book_id = input("Enter the book ID to remove: ")
            library.remove_book(book_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

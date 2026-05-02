
import sqlite3
from database import create_tables
from operations import add_book, view_books, issue_book, return_book

def menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            add_book(title, author)

        elif choice == '2':
            view_books()

        elif choice == '3':
            book_id = int(input("Enter book ID to issue: "))
            issue_book(book_id)

        elif choice == '4':
            book_id = int(input("Enter book ID to return: "))
            return_book(book_id)

        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    create_tables()
    menu()

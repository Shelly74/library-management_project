
from database import connect

def add_book(title, author):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()

    print("Book added successfully!")

def view_books():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\nID | Title | Author | Available")
    print("---------------------------------")
    for book in books:
        print(book)

    conn.close()

def issue_book(book_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT available FROM books WHERE id=?", (book_id,))
    result = cursor.fetchone()

    if result and result[0] == 1:
        cursor.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        conn.commit()
        print("Book issued successfully!")
    else:
        print("Book not available!")

    conn.close()

def return_book(book_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

    print("Book returned successfully!")

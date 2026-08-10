# Library Management System


books = []


def add_book():
    book = input("Enter book name: ")
    author = input("Enter author name: ")

    books.append({
        "name": book,
        "author": author,
        "status": "Available"
    })

    print("Book added successfully!")


def view_books():

    if len(books) == 0:
        print("No books available.")
        return

    print("\n----- BOOK LIST -----")

    for i in range(len(books)):
        print("Book ID:", i + 1)
        print("Book Name:", books[i]["name"])
        print("Author:", books[i]["author"])
        print("Status:", books[i]["status"])
        print("--------------------")


def search_book():

    name = input("Enter book name to search: ")

    found = False

    for book in books:

        if book["name"].lower() == name.lower():

            print("\nBook Found!")
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("Status:", book["status"])

            found = True

    if found == False:
        print("Book not found.")


def issue_book():

    view_books()

    if len(books) == 0:
        return

    book_id = int(input("Enter Book ID to issue: "))

    if book_id < 1 or book_id > len(books):
        print("Invalid Book ID.")
        return

    book = books[book_id - 1]

    if book["status"] == "Available":

        book["status"] = "Issued"

        print("Book issued successfully!")

    else:

        print("Book is already issued.")


def return_book():

    view_books()

    if len(books) == 0:
        return

    book_id = int(input("Enter Book ID to return: "))

    if book_id < 1 or book_id > len(books):
        print("Invalid Book ID.")
        return

    book = books[book_id - 1]

    if book["status"] == "Issued":

        book["status"] = "Available"

        print("Book returned successfully!")

    else:

        print("This book is not issued.")


def delete_book():

    view_books()

    if len(books) == 0:
        return

    book_id = int(input("Enter Book ID to delete: "))

    if book_id < 1 or book_id > len(books):
        print("Invalid Book ID.")
        return

    books.pop(book_id - 1)

    print("Book deleted successfully!")




while True:

    print("\n================================")
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
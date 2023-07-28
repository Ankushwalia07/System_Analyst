''' Database Design and Management. For this advanced Python code example,
 let's create a simple command-line address book application.
  The application will allow users to add, view, update, and delete contacts.
 We'll use the SQLite database to store and manage the contacts.'''
import sqlite3

def create_table():
    connection = sqlite3.connect("address_book.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def add_contact(name, phone, email):
    connection = sqlite3.connect("address_book.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    connection.commit()
    connection.close()
    print("Contact added successfully!")

def view_contacts():
    connection = sqlite3.connect("address_book.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    connection.close()
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")

def update_contact(contact_id, name, phone, email):
    connection = sqlite3.connect("address_book.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, contact_id))
    connection.commit()
    connection.close()
    print("Contact updated successfully!")

def delete_contact(contact_id):
    connection = sqlite3.connect("address_book.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    connection.commit()
    connection.close()
    print("Contact deleted successfully!")

def main():
    create_table()

    while True:
        print("\nAddress Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            add_contact(name, phone, email)

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            contact_id = int(input("Enter the contact ID to update: "))
            name = input("Enter the updated name: ")
            phone = input("Enter the updated phone number: ")
            email = input("Enter the updated email address: ")
            update_contact(contact_id, name, phone, email)

        elif choice == "4":
            contact_id = int(input("Enter the contact ID to delete: "))
            delete_contact(contact_id)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

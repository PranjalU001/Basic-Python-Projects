import pandas as pd
import random

# Creating the CSV files if they don't exist
def create_csv(file):
    columns = ['Book ID', 'Title', 'Author', 'Availability']
    try:
        pd.read_csv(file)
    except FileNotFoundError:
        pd.DataFrame(columns=columns).to_csv(file, index=False)

def create_student_csv(file):
    columns = ['Book ID', 'Student Name', 'Registration No', 'Branch', 'Email']
    try:
        pd.read_csv(file)
    except FileNotFoundError:
        pd.DataFrame(columns=columns).to_csv(file, index=False)

class Library:
    def __init__(self, file, student_file):
        self.file = file
        self.student_file = student_file
        self.df = pd.read_csv(self.file)
        self.student_df = pd.read_csv(self.student_file)

    def add_books(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        availability = "Available"
        new_book = pd.DataFrame([[book_id, title, author, availability]], columns=['Book ID', 'Title', 'Author', 'Availability'])
        self.df = pd.concat([self.df, new_book], ignore_index=True)
        self.df.to_csv(self.file, index=False)
        print(f"Book '{title}' added successfully!")

    def issue_books(self):
        book_id = input("Enter Book ID to issue: ")
        if book_id in self.df['Book ID'].values:
            book_row = self.df[self.df['Book ID'] == book_id]
            if book_row['Availability'].values[0] == "Available":
                # Collect student details
                student_name = input("Enter Student Name: ")
                reg_no = input("Enter Registration Number: ")
                branch = input("Enter Branch: ")
                email = input("Enter Email: ")
                
                # Update book status to issued
                self.df.loc[self.df['Book ID'] == book_id, 'Availability'] = "Issued"
                self.df.to_csv(self.file, index=False)

                # Store student details
                new_student = pd.DataFrame([[book_id, student_name, reg_no, branch, email]], 
                                           columns=['Book ID', 'Student Name', 'Registration No', 'Branch', 'Email'])
                self.student_df = pd.concat([self.student_df, new_student], ignore_index=True)
                self.student_df.to_csv(self.student_file, index=False)
                
                print(f"Book ID '{book_id}' has been issued to {student_name}.")
            else:
                print(f"Book ID '{book_id}' is already issued.")
        else:
            print("Book not found!")

    def return_books(self):
        book_id = input("Enter Book ID to return: ")
        if book_id in self.df['Book ID'].values:
            # Update the book status to available
            self.df.loc[self.df['Book ID'] == book_id, 'Availability'] = "Available"
            self.df.to_csv(self.file, index=False)
            
            # Retrieve and display student details
            student_row = self.student_df[self.student_df['Book ID'] == book_id]
            if not student_row.empty:
                print("Book returned by:")
                print(student_row[['Student Name', 'Registration No', 'Branch', 'Email']])
                
                # Remove student details after the book is returned
                self.student_df = self.student_df[self.student_df['Book ID'] != book_id]
                self.student_df.to_csv(self.student_file, index=False)
            else:
                print("No student information found.")
            
            print(f"Book ID '{book_id}' has been returned.")
        else:
            print("Book not found!")


# Main Menu for User Interaction
def menu():
    book_file = 'library_books.csv'
    student_file = 'students.csv'
    create_csv(book_file)  # Ensure the CSV file for books is created
    create_student_csv(student_file)  # Ensure the CSV file for students is created
    library = Library(book_file, student_file)

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.add_books()
        elif choice == 4:
            library.issue_books()
        elif choice == 5:
            library.return_books()
        elif choice == 6:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Running the menu
menu()

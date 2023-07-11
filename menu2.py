import csv
from books import Book
from borrower import Borrower
from transactions import Transaction
from datetime import datetime
def selection_validate():
    valid_selections = ('1', '2', '3', '4', '5', '6')
    message = input("Welcome to the main menu. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':
        selection = input("\nPlease select from the following menu (Type exit to exit program) \n"
                        "To request a new loan enter 1 \n"
                        "To return a book enter 2 \n"
                        "To extend a loan enter 3 \n"
                        "To add a user enter 4 \n"
                        "To update a user enter 5 \n"
                        "To add a book enter 6 \n"
                        "\nEnter choice: ")
        if selection == 'exit':
            break
        else:
            if selection in valid_selections:
                loop = 'no'
            else:
                print('\nValue: {} did not match any menu choice'.format(selection))
                loop = 'yes'
    return selection
def selection_calls():
    selection = selection_validate()
    if selection == '1':
        print("You can request a book here")
        member_id = input('Enter your Member ID:')

        borrower = Borrower(None, None, None, None)
        book = Book(None, None, None, None, None, None, None)

        member = borrower.search_user_by_member_id(member_id)
        if member:
            with open('book_data.csv', 'r') as book_file:
                for row in book_file:
                    print(row)
            book_title = input("Which book do you want to borrow?: ")

            found = book.search_book_by_title(book_title)
            if found:
                borrow_date = datetime.now().strftime("%d/%m/%y")
                due_date = input("Enter return date in mm/dd/yy format: ")
                return_date = input("Enter actual return date in mm/dd/yy format: ")
                
                borrow_book = Transaction(member_id=member_id,book_title=book_title, borrow_date=borrow_date, due_date=due_date, return_date=return_date)
                borrow_book.transaction_data()
            else:
                print("Sorry, we don't have this book.")
        else:
            print("Member Not Found")
            
    elif selection == '2':
        member_id = input("Please enter your member ID: ")

        found_books = []
        with open('transaction.csv', 'r+') as file:
            for line in file:
                borrowed_details = line.strip().split(',')
                if borrowed_details[1] == member_id:
                    found_books.append(borrowed_details)

        if found_books:
            print('These are the borrowed books:')
            for book in found_books:
                print(','.join(book))

            is_return = True
            while is_return:
                book_to_return = input("Please enter a book title you want to return: ")
                for book in found_books:
                    if book[0] == book_to_return:
                        found_books.remove(book)
                        with open('transaction.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(found_books)

                        with open('book_data.csv', 'r') as file:
                            reader = csv.reader(file)
                            rows = list(reader)
                            for row in rows:
                                if row[2] == book_to_return:
                                    row[4] = str(int(row[4]) + 1)
                                    break

                        with open('book_data.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)
                        print("Book returned successfully!")
                    

            another_book_return = input("Do you want to return any other books (Yes/No): ").lower()
            if another_book_return == "no":
                is_return = False
        else:
            print('No borrowed books found for your membership ID.')
    
    elif selection == '3':
        membership_id = input("Please enter your membership ID: ")
        found_books = []

        with open('transaction.csv', 'r+') as file:
            for line in file:
                borrowed_details = line.strip().split(',')
                if borrowed_details[1] == membership_id:
                    found_books.append(borrowed_details)

        if found_books:
            print('These are the borrowed books found in our database for you:')
            for book in found_books:
                print(','.join(book))

            extend = True
            while extend:
                book_to_extend = input("Please enter a book title for the book you want to extend: ")
                for book in found_books:
                    if book[0] == book_to_extend:
                        new_date = input("Please enter a new return date in mm/dd/yy format: ")
                        book[3] = new_date

                        with open('transaction.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(found_books)
                        print("Return Date Updated successfully!")

                    extend = False
        else:
            print('No borrowed books found for your membership ID.')
        
    elif selection == '4':
        name = input('Enter Borrower Name:')
        email = input('Enter Email:')
        birthdate = input('Enter Birth Day:')
        member_id = input('Enter Member ID:')
        
        new_user = Borrower(name=name, email=email, birthdate=birthdate , member_id = member_id)
        new_user.add_user()
        
    elif selection == '5':
        email = input('Enter Email:')            
        user_update = Borrower(None, None, None, None)
        found = user_update.search_user_by_email(email)
        if found:
            print("User found.")
            name = input('Enter new User Name:')
            email = input('Enter new User Email:')
            birthdate = input('Enter new Birth Day:')
            member_id = input("Enter new Member ID:")
            user_update.update_user(name,email, birthdate, member_id)
        else:
            print("User not found.")
        
        
    elif selection == '6':
        book_id = input("Enter book ID:")
        book_name = input("Enter book name:")
        title = input("Enter title:")
        author = input("Enter author:")
        quantity = input("Enter quantity:")
        pub_year = input("Enter year published:")
        edition = input("Enter edition:")
        
        
        new_book = Book(book_id=book_id, book_name=book_name, title=title, author=author, quantity=quantity, pub_year=pub_year, edition=edition)
        new_book.add_book()
        
   

if __name__ == '__main__':
    selection_calls()
    
    
    

import csv
import datetime

class Transaction:
    counter = 0
    Due_Duration = 7

    def __init__(self, member_id, book_title, borrow_date, due_date,return_date):
        Transaction.counter += 1
        self.transaction_id = Transaction.counter
        self.book_title = book_title
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date

    def transaction_data(self):
        transaction_detail = f"{self.member_id},{self.book_title},{self.borrow_date},{self.due_date},{self.return_date}\n"
        with open("transaction.csv", "a") as file:
            file.write(transaction_detail)
        print("Transaction Successful!!!")
        
    @staticmethod
    def update_return_book(member_id):
        transactions = []
        transaction_found = False

        with open("transaction.csv", "r+") as file:
            for line in file:
                line_list = line.strip().split(",")
                if line_list[1] == member_id and line_list[5] == "None":
                    line_list[5] = str(datetime.date.today())
                    line = ','.join(line_list)
                    transaction_found = True
                transactions.append(line + "\n")

        if transaction_found:
            with open("transaction.csv", "w") as file:
                file.writelines(transactions)
        else:
            print("No Transaction Found. ")
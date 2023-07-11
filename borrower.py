import csv

class Borrower():
    
    def __init__(self,name,email,birthdate,member_id):
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.member_id = member_id
        
        
    def add_user(self):
        user_data = f"{self.name}---{self.email}---{self.birthdate}---{self.member_id}\n"
        found = self.search_user_by_member_id(self.member_id)
        
        if not found:
            with open("borrower_data.csv", "a+") as file:
                file.write(user_data)
               
            print("User added successfully")
        else:
            print("User already exists")

    def search_user_by_email(self, email):
         with open("borrower_data.csv", "r") as file:
            for line in file:
                borrower_info = line.strip().split("---")
                if len(borrower_info) >= 4 and borrower_info[1] == email:
                    return True


    def search_user_by_member_id(self, member_id):
        with open("borrower_data.csv", "r") as file:
            for line in file:
                borrower_info = line.strip().split("---")
                if len(borrower_info) >= 4 and borrower_info[3] == member_id:
                    return True

        return False
    
    def update_user(self, name, email, birthdate, member_id):
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.member_id = member_id
        new_data = f'{self.name}---{self.email}---{self.birthdate}---{self.member_id}'
        with open("borrower_data.csv", "r+") as file:
            file.write(new_data)
        
        print("Updated successfully")

import os 
import csv 


new_csv_name = "db.csv"
# create new row to add 
class operations():
    def __init__(self):
        self.choice = int(input("1 : New Item. \t2 : Read Item: "))
        if self.choice == 1:
            self.add()
        else: 
            print("broken")

    def add(self):
        self.login_name = input("Enter the name of the login name: ")
        self.username = input("Enter the username: ")
        self.email = input("Enter the email: ")
        self.passowrd = input("Enter the passowrd: ")
        self.notes = input("Any Additional notes?: ")
        self.new_row = [login_name, username, email, passowrd, notes]
        return self.new_row


test_list = ["reddit", "suhib", "me@gmail.com", "123456",""]

with open(new_csv_name, 'a') as newFile:
    newFileWriter = csv.writer(newFile)
    # x = operations() 
    newFileWriter.writerow(test_list)

with open(new_csv_name,'r') as newFile:
    newFileReader = csv.reader(newFile)
    for row in newFileReader:
        print (row)
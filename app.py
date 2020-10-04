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
        self.new_row = [self.login_name, self.username, self.email, self.passowrd, self.notes]

        with open(new_csv_name, 'a') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow(self.new_row)


operations()



with open(new_csv_name,'r') as newFile:
    newFileReader = csv.reader(newFile)
    for row in newFileReader:
        print (row)
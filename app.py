import os 
import csv 


new_csv_name = "db.csv"
# create new row to add 
def add():
    login_name = input("Enter the name of the login name: ")
    username = input("Enter the username: ")
    email = input("Enter the email: ")
    passowrd = input("Enter the passowrd: ")
    notes = input("Any Additional notes?: ")
    new_row = [[login_name, username, email, passowrd, notes]]
    return new_row

# work on this 

# def check():
#     choice_1 = input("1 : New Item. \t2 : Read Item: ")
#     if  choice_1 == 1:
#         return add()

# create new csv file 

# later when we will have multiple databases
# new_csv_name = input("Enter the new Database name: ")
# new_csv_name = new_csv_name + ".csv"


with open(new_csv_name, 'a') as newFile:
    newFileWriter = csv.writer(newFile)
    x = add() 
    newFileWriter.writerow(x)

with open(new_csv_name,'r') as newFile:
    newFileReader = csv.reader(newFile)
    for row in newFileReader:
        print (row)
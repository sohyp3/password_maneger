import os 
import csv 

# create new csv file 
def add():
    login_name = input("Enter the name of the login name: ")
    username = input("Enter the username: ")
    email = input("Enter the email: ")
    passowrd = input("Enter the passowrd: ")
    notes = input("Any Additional notes?: ")
    new_row = [[login_name, username, email, passowrd, notes]]
    return new_row

def check():
    choice_1 = input("1 : New Item. \t2 : Read Item: ")
    if  choice_1 == 1:
        return add()

    



new_csv_name = input("Enter the new Database name: ")
new_csv_name = new_csv_name + ".csv"
with open (new_csv_name, 'w') as new_file:
    writer = csv.writer(new_file)
    x = add()
    writer.writerows(x)
        





import os 
import csv 
import sys


# Ask the password 

master_password = "pineapple"
not_equal_0 = 1
sec_counter = 0
while not_equal_0 !=0:
    entery_for_password = input("Please Enter the master Password: ")
    if entery_for_password != master_password:
        sec_counter += 1
        print("Wrong Try again")
    else:
        print("Welcome")
        not_equal_0 = 0
    if sec_counter == 3 :
        not_equal_0 = 0
        print("\ntoo many wrong attempts GTFO :3\n")
        sys.exit()

# ==========================================================================================         

new_csv_name = "db.csv"

class operations():
    def __init__(self):
        self.choice = int(input("1 : New Item. \t2 : Search For Item. \t3 : Edit an Item. \t 4 : Remove an Item. \n: "))
        if self.choice == 1:
            self.add()
        else: 
            print("broken")


    def add(self):

        self.username = input("Enter the username: ")
        self.email = input("Enter the email: ")
        self.passowrd = input("Enter the passowrd: ")
        self.notes = input("Any Additional notes?: ")
        self.new_row = [self.login_name, self.username, self.email, self.passowrd, self.notes]


    def remove(self,selected):
        pass

    def edit(self,seleceted):
        are_you_sure = input("Are you Sure? (Y/n) ").lower
        if are_you_sure == "y":
            print("kk dude do it if u dare")
            
        else :
            print("ok bye")
    def search(self,keyword):
        pass 
    
    def showall(self):
        pass


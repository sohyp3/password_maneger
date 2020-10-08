import sys
import os
import sqlite3


database = "pswd.db"


class functions():
    def __init__(self):
        self.passowrd_check()
        self.file_check()

    def passowrd_check(self):
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

    def file_check(self):
        if os.path.isfile(database):
            pass 
        else : 
            with (open(database,"w")):
                print("Database Created!")


class operations():
    def __init__(self):
        print("Hai")


    def add (self):
        self.username = input("Enter the username: ")
        self.email = input("Enter the email: ")
        self.passowrd = input("Enter the passowrd: ")
        self.notes = input("Any Additional notes?: ")
        return [self.username, self.email,self.passowrd, self.notes]

    def remove(self,id):
        pass 

    def update(self,update_selection,update_item):
        pass 

    def remove(self,id):
        pass 

    def showall(self):
        pass
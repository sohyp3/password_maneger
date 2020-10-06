import os 
import csv 
import sys


# Ask the password 
#
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


    def remove(self,selected):
        #idk how to but remove the seleceted
        pass
    def edit(self,seleceted):
        are_you_sure = input("Are you Sure? (Y/n) ").lower
        if are_you_sure == "y":
            #do it somehow 
            print("kk dude do it if u dare")
        else :
            print("ok bye")
    def search(self,keyword):
        pass 
        # check for it too 
    
    def showall(self):
        with open('user.csv','r') as userFile:
            userFileReader = csv.reader(userFile)
            for row in userFileReader:
                print (row)


# ==========================================================================================
check_db = os.path.isfile(new_csv_name)
if check_db:
    print("found welcome")
else: 
    with open(new_csv_name, 'w') as newFile:
        newFileWriter = csv.writer(newFile)    
    print("Just Created one!")

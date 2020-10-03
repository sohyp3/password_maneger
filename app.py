import os 
import csv 


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
        self.new_row = [[login_name, username, email, passowrd, notes]]
        return self.new_row
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



# check for the dir 
# currently disabled because the multiple databases feature will be added later! 

# check_dir = os.path.isdir("databases")
# if check_dir:
#     print("Folder Found")

# else: 
#     os.mkdir("databases")
#     print("Created New Directory!")


check_db = os.path.isfile("db.csv")
if check_db:
    print("found welcome")
else: 
    with open(new_csv_name, 'w') as newFile:
        newFileWriter = csv.writer(newFile)    
    print("Just Created one!")

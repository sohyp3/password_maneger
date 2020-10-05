import os 
import csv 


new_csv_name = "db.csv"
# create new row to add 
class operations():
    def __init__(self):
        self.choice = int(input("1 : New Item. \t2 : Search for Item: "))
        if self.choice == 1:
            self.add()
        elif self.choice == 2: 
            self.search()
        else:
            print("BRoKEn!")

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

    def remove(self):
        self.remove_item = input("Please Enter the item you want to remove: ")
        

    def search(self):
        self.search_for = input("Tell me What are you looking for? ")
        with open (new_csv_name,'r') as newFile:
            newFileReader = csv.reader(newFile)

            for word in newFileReader:
                if self.search_for in word:
                    print(word)
                else :
                    for specific_search in word:
                        if self.search_for in specific_search:
                            print(word)



operations()



# with open(new_csv_name,'r') as newFile:
#     newFileReader = csv.reader(newFile)
#     for row in newFileReader:
#         print (row)
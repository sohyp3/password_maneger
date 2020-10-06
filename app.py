import os 
import csv 


new_csv_name = "db.csv"
# create new row to add 
class operations():
    def __init__(self):
        self.choice = int(input("1 : New Item. \t2 : Search for Item \t3 : for edit  \t4 : for remove \n: "))
        if self.choice == 1:
            self.add()
        elif self.choice == 2: 
            self.search()
        elif self.choice ==3:
            self.edit()
        elif self.choice == 4: 
            self.remove()
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
        self.remove_item = input("Enter the Login name that you want to delete: ")


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
    
    def edit(self):
        with open(new_csv_name ,"r") as newFile:
            readie = csv.reader(newFile)
            for word in readie:
                print(word)

        self.edit_file = input ("Which login you want to edit? ")

        with open (new_csv_name ,"r")as newFile:
            readie = csv.reader(newFile)
            
            with open ("temp.csv","w") as newFile2:
                writie = csv.writer(newFile2)
                

                for  word in readie:
                    if self.edit_file in word[0]:
                        print(word)
                        are_you_sure = input("are you sure?? (Y/n)").lower
                        if are_you_sure == "n":
                            break
                        

                        test_list = ["reddit","yollo", "mollo@noonelikesyou.com", "ferystrongpasswerd",""]
                        
                        writie.writerow(test_list)
                    else: 
                        writie.writerow(word)

        with open (new_csv_name, "w") as newFile3:
            writie = csv.writer(newFile3)
            with open ("temp.csv","r") as newFile2:
                readie = csv.reader(newFile2)

                for word in readie:
                    writie.writerow(word)
                




                    








operations()



# with open(new_csv_name,'r') as newFile:
#     newFileReader = csv.reader(newFile)
#     for row in newFileReader:
#         print (row)
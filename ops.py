import sys
import os
import sqlite3
import random 


#SQLite stuff
database = "passwords.db"
conn = sqlite3.connect(database)
c = conn.cursor()



class functions():
    def __init__(self):
        # self.passowrd_check()
        # self.file_check()
        self.table_check()
        operations().showall()
        operations().search()
        # lenghth = int(input("Please Enter the Len of the password : "))
        #self.password_generate(lenghth)

    def table_check(self):
        with conn:
            c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='passwords'; ''')
            if c.fetchone()[0]==1 : {
                print('Table exists.')
            }
            else:
                c.execute("""CREATE TABLE passwords (
                            id INTEGER PRIMARY KEY,
                            login text,
                            email text,
                            username text,
                            pswd text,
                            notes text
                            );""") 
                print("Table has been created.")


        

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
    
    # There is no need since the sqlite creates one already if its not there 
    # def file_check(self):
    #     if os.path.isfile(database):
    #         pass 
    #     else : 
    #         with (open(database,"w")):
    #             print("Database Created!")


    def password_generate(self,lenghth):
        self.leng = lenghth
        letters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+|"
        result_str = ''.join((random.choice(letters) for i in range(self.leng)))
        return result_str


class operations():
    def __init__(self):
        print("Hai")


    def info_get (self):
        self.login = input("Ente the login name: ")
        self.email = input("Enter the email or phone number: ")
        self.username = input("Enter the username: ")
        self.passowrd = input("Enter the passowrd: ")
        self.notes = input("Any Additional notes?: ")
        return [self.login ,self.email, self.username,self.passowrd, self.notes]



    def add(self):
        insert = self.info_get()
        with conn:
            c.execute("INSERT INTO passwords(login, email, username, pswd, notes) VALUES (:login, :mail, :user , :pswd , :notes)", {'login': insert[0], 'mail': insert[1] , 'user': insert[2], 'pswd' :insert[3], 'notes':insert[4]})        
            c.execute("SELECT * FROM passwords")
            print(c.fetchall())


    def update(self,update_selection,update_item):
        pass 

    def remove(self,id):
        pass 
    
    def search(self):
        search_for = input("What Are you looking for: ")
        with conn:
            c.execute("SELECT * FROM passwords WHERE login = :srch", {'srch' : search_for})
            print(c.fetchall())

    def showall(self):
        with conn:
            c.execute("SELECT * FROM passwords")
            items = c.fetchall()
            for item in items:
                print(item)



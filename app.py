import sys
import sqlite3
import random


master_password = 'banana'

# SQLite Connection()
database = 'passwords.db'
conn = sqlite3.connect(database)
c = conn.cursor()

class home():
    def __init__(self):
        self.password_check()
        self.table_check()
        
        operations()

    def table_check(self):
        with conn:
            c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='passwords'; ''')

            if c.fetchone()[0] ==1:
                print('Table Exists')

            else:
                c.execute(""" 
                    CREATE TABLE passwords(
                        id INTEGER PRIMARY KEY,
                        login text,
                        email text,
                        username text,
                        pswd text,
                        notes text,
                        );
                """)
                print('Table Exists')

    def password_check(self):
        tries = 0

        while True:
            password_input = input("Enter the master password: ")
            if password_input != master_password:
                tries += 1
                print('Wrong, Try again')
            else:
                print('Welcome')
                break
            
            if tries == 3:
                print('Too many wrong attempt, bye!')
                sys.exit()



def generate_password(length):
    letters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+|"

    return "".join(random.choice(letters) for i in range(length))





class operations():
    def __init__(self):
        self.show_all()
        choice = input('(A)dd \n(S)earch\n(U)pdate\n(R)emove\nChoose: ')

        if choice.lower() == 's':
            self.search()
        elif choice.lower() == 'a':
            self.add()
        elif choice.lower() == 'u':
            self.update()
        elif choice.lower() == 'r':
            self.remove()


    def show_all(self):
        with conn:
            c.execute('SELECT * FROM passwords')
            items = c.fetchall()
            for item in items:
                print(item)


    def search(self):
        search_for = input('Enter the login to search for remove: ')
        with conn:
            c.execute('SELECT * FROM passwords WHERE login LIKE ?',(f'%{search_for}%',))
            print(c.fetchall())
            
    def remove(self):
        search_for = input('What are you looking for: ')
        with conn:
            c.execute('SELECT * FROM passwords WHERE login LIKE ?',(f'%{search_for}%',))
            print(c.fetchall())

            self.del_sel = int(input("Select the id for the item you want to remove: (0 to exit)  "))
            if self.del_sel == 0:
                print('exiting..')
            else:
                c.execute("SELECT *  FROM passwords WHERE id = ?",(self.del_sel,))
                print(c.fetchall())
                self.del_sure = input('Are you sure? (y/N): ')
                if self.del_sure.lower() == 'y':
                    c.execute("DELETE FROM passwords WHERE id = ?",(self.del_sel,))
                    print('deleted!')
                    print('======\n=====\n=====\n=====\n====\n')
                    self.show_all()
                else:
                    print('aborted!')




    def update(self):
        search_for = input('Enter the login to search for update: ')
        with conn:
            c.execute('SELECT * FROM passwords WHERE login LIKE ?', (f'%{search_for}%',))
            print(c.fetchall())

            self.upd_sel= int(input("Select the id for the item you want to update: (0 to exit) "))
            if self.upd_sel== 0:
                print('Exiting...')
            else:
                self.field_to_update = input("What do you want to update? (login/email/username/password/notes): ").lower()

                self.new_value = input(f"Enter new {self.field_to_update}: ")

                c.execute(f"UPDATE passwords SET {self.field_to_update} = ? WHERE id = ?", (self.new_value, self.upd_sel))
                print('Updated successfully!')

                print('======\n=====\n=====\n=====\n====\n')
                self.show_all()

    def add(self):
        self.login = input("login name: ")
        self.email = input("email or phone number: ")
        self.username = input("username: ")

        self.gen_pass = input("do you want to generate a password? (Y/n): ")
        if self.gen_pass.lower() !='n' :
            length = int(input('how long you want it to be? '))
            self.password = generate_password(length)
            print(f"selected password : {self.password}")
        else:
            self.password= input("passowrd: ")
        self.notes = input("notes: ")


        with conn:
            c.execute("INSERT INTO passwords(login, email, username, pswd, notes) VALUES (? , ? , ? , ? ,?)",(self.login,self.email,self.username,self.password,self.notes))
            self.show_all()





home()

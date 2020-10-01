import os 
import csv 

new_csv_name = "db.csv"
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

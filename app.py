import os 

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
    
    print("Just Created one!")

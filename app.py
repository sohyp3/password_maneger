import os 

check_dir = os.path.isdir("databases")
if check_dir:
    print("Folder Found")

else: 
    os.mkdir("databases")
    print("Created New Directory!")




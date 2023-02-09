import os

# Open the text file containing the list of files to delete
with open('file_list.txt', 'r') as file:
    # Read the list of files
    file_list = file.readlines()

# Iterate through the list of files
for file_name in file_list:
    # Remove the newline character from the file name
    file_name = file_name.strip()
    if os.path.isfile(file_name):
        # Delete the file
        os.remove(file_name)
        #print("found.")
    else:
        print(f"{file_name} not found.")

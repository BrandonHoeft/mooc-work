# context manager to open and write a file to disk. 
with open(home + desktop_rel_path + '/my_file.txt', 'w') as f:   # open this file using the writing mode, and call it f. 
    f.write('Hello, World!') # automatically closes

# Read File
with open(home + desktop_rel_path + '/my_file.txt', 'r') as f:   
    print(f.readlines())

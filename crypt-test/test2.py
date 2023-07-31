import bcrypt


what_file = input("what file: ") 
file = open(what_file, 'r')
print(file.read())

#the bellow line is the hashed password from the file 
masterpassfromfile = file.read()


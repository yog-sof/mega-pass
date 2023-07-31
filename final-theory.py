import bcrypt

#encryption
password = str(input("input password: "))
password = password.encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))

#writes the hashed password to a file after getting it 
#input by the user 
print("Encrypted password: ", hashed)
print("Copy the encrypted password here to save it")
hash_verify = input(">:")
file = open("masterpass.dat", "w")
file.write(hash_verify)

#taking the text from the masterpass.dat file and encoding it with utf-8
print("***************")
print("check password with encryption")
check = str(input(">:"))
check = check.encode('utf-8')
print("now checking if user input password matches the hash from file")
if bcrypt.checkpw(check, hashed):
    print("login works")
else:
    print("not working")

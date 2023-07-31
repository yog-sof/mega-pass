import bcrypt

#encryption
password = str(input("input password: "))

password = password.encode('utf-8')

hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))

#decryption 
check = str(input("check password: "))

check = check.encode('utf-8')

if bcrypt.checkpw(check, hashed):
    print("login yes")
else: 
    print("NONONONONONO")

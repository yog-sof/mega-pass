from generator import gen
from logo import logo
from manager import manager
import os 
import time 

while True: 
    time.sleep(1)
    os.system("clear")
    logo()
    print("menu:\n 1) Password Generator\n 2) Password Manager\n 3) help\n 4) quit")
    choice = int(input(">:"))

    if choice == 1:
        gen()

    elif choice == 2: 
        manager()
        

    elif choice == 3: 
        print("Mega-Pass can generate you strong randomized passwords")
        print("as well as storing your passwords in a password manager") 
        print("You can have different profiles where you can store files inside of")
        print("for your different identetis (eg: Personal / Professional)")
        print("This is to help you have better organisation")
        print()
        print("press enter to continue")
        input("")

    elif choice == 4: 
        quit()

    else: 
        print("invalid option")
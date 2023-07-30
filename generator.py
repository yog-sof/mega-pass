import random
import string 

#ideas:
# to have an option to add it to the password manager 
# by calling in that function from the manager file 

def gen():
    print("********************")
    print(" Password generator ")
    print("********************")
    def generate_password(min_length, numbers=True, special_characters=True):
        letters = string.ascii_letters
        digits = string.digits
        special = string.punctuation

        characters = letters 
        if numbers: 
            characters += digits
        if special_characters:
            characters += special
    
        pwd = ""
        meets_criteria = False 
        has_number = False
        has_special = False 

        #Ensures that the password contains all requirements 
        while not meets_criteria or len(pwd) < min_length:
            new_char = random.choice(characters)
            pwd += new_char


        #seeing what is required 
            if new_char in digits: 
                has_number = True 
            elif new_char in special: 
                has_special = True 


        #seeing if criteria is met
            meets_criteria = True 
            if numbers:
                meets_critera = has_number
            if special_characters:
                meets_criteria = has_special


        #at the end returning the generated password
        return pwd

    #The menu option which will call in the function of generate_password with the information from 
    #the user input (bellow) 
    min_length = int(input("Enter minimum size:"))
    has_number = input("do you want to include integers (y/n):").lower() == "y"
    has_special = input("do you want to include special characters (y/n):").lower() == "y"
    pwd = generate_password(min_length, has_number, has_special)
    print("Password: ", pwd)
    print("press enter to leave")
    input()

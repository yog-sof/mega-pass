import os 
from cryptography.fernet import Fernet
def view_profile_list():
    os.system("cd profiles && ls") 


def showprofilelist():
    os.system("cd profiles && ls")


def make_profile():
    print("What is the name of the profile you want to create (no spaces)") 
    name_new_profile = input(">:")
    command = "cd profiles && mkdir " + name_new_profile
    os.system(command)




def view():
    #view profile function
    print("********************")
    print("What profile do you want to view") 
    chosen_profile = input(">:")
    show_profile_content = "cd " + "profiles/" + chosen_profile + " && ls" 
    os.system(show_profile_content)
    print("What file do you want to view")
    chosen_file = input(">:")
    file_path = "profiles/" + chosen_profile + "/" + chosen_file
    read_file_command = "cat " + file_path
    os.system(read_file_command)
    


    
    
   



def add(): 
    #adds to profile function 
    print("********************")
    print("What profile do you want to add to") 
    chosen_profile = input(">:")
    print("What is the name of the service this account is for") 
    filename1 = input(">:")
    file_name = filename1 + ".dat"

    print("Now store the information") 
    user = input("Account username: ")
    pwd = input("Account Password: ")

    with open(file_name, 'a') as f: 
        f.write("ACCOUNT NAME: " + user + "\nPASSWORD: " + pwd + "\n")






















    move_to_profile_command = "mv " + file_name + " profiles/" + chosen_profile 
    os.system(move_to_profile_command)

def manager(): 
  print("*******************")
  print("What is the master password?")
  master_pwd = input(">:")
  print("*******************")
  print(" 1) create new profile\n 2) add to profile (unfinished)\n 3) view profile (unfinished)\n")
  choice = int(input(">:"))

  if choice == 1: 
      make_profile()
  elif choice == 2: 
      view_profile_list()
      add()
  elif choice == 3: 
      view_profile_list()
      view()


  else: 
     print("Invalid input")
  print()
  print("press enter to continue") 
  input("")

import os
from sys import exit

from utils.login import login
from utils.signup import signup

def Welcome(error: str):
    os.system('cls')
    print("")
    print("Welcome to the Authentication Program, by budzHors7")
    print("")
    print("Authentication is needed to continue...")
    if error != "":
        print(error)
    print("")
    print("========================== Authentication ==========================")
    print("")
    print("1: Login                  2: Sign-up")
    print("----------------------------------------------------------------------")
    print("3: Quit App")
    print("")
    print("=====================================================================")
    print("")

    selection = int(input("Select Menu : "))

    if selection == 1:
        login()

    elif selection == 2:
        signup()

    elif selection == 3:
        os.system('cls')
        exit()
    
    else:
        Welcome("Wrong Selection, only 1/2 available as options.")

Welcome("")
import os
import json
from getpass import getpass
from time import sleep
from bcrypt import gensalt, hashpw
from hashlib import sha256

user = {
    'username': '',
    'password': ''
}

def login():
    os.system('cls')
    print("")
    print("========================== Login ==========================")
    print("")
    username = input("Enter your username: ")
    print("")
    password = getpass("Enter your password: ")
    print("")
    print("Please wait...")
    sleep(5)
    print("")
    verifyPass = checkLogin(username, password)
    print("")
    if verifyPass == True:
        input("\nLogged is successful, \nClick enter/return to continue to your profile.")

        from utils.profile import profile
        profile()
    else:
        selection = input("\nLogged unsuccessful, \nClick 'r' to retry or enter/return to return home.\n->: ")

        if selection == "r":
            login()
        elif selection == "":
            from app import Welcome

            Welcome()

def checkLogin(username: str, password: str) -> bool:
    loadFile()

    generatePassword = password.encode()
    salt = gensalt()

    generateBytes = hashpw(generatePassword, salt)
    generateHash = sha256(generateBytes).hexdigest()

    print(
        "\nPassword: " + password +
        "\nHashedPass: " + user["password"]
    )

    if username != user["username"]:
        print("Wrong Username")
        return False
    
    elif generateHash != user["password"]:
        print("Wrong Password")
        
    else:
        return True
    
def loadFile():
    with open("./tokens/users.json", "r") as json_file:
        json_object = json.load(json_file)

    for users in json_object["users"]:
        user["username"] = users["username"]
        user["password"] = users["password"]

    return user
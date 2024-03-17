import os
from json import dumps
from uuid import uuid4
from getpass import getpass
from time import sleep
from bcrypt import gensalt, hashpw
from hashlib import sha256

def signup():
    os.system('cls')
    print("")
    print("========================== Sign Up ==========================")
    print("")
    username = input("Enter your username: ")
    print("")
    password = getpass("Enter your password: ")
    print("")
    print("Please wait...")
    sleep(5)
    print("")
    registration(username, password)
    print("")
    input("\nRegistration done, \nClick enter/return to return to Welcome Page.")

    from app import Welcome
    Welcome("")

def registration(username: str, password: str):

    generateUserId = uuid4()
    generatePassword = password.encode()

    salt = gensalt()

    generateBytes = hashpw(generatePassword, salt)
    generateHash = sha256(generateBytes).hexdigest()

    user = {
        "users": [
            {
                "username": username,
                "userid": str(generateUserId),
                "password": generateHash
            }
        ]
    }

    json_object = dumps(user, indent = 4)

    with open("./tokens/users.json", "w") as json_file:
        json_file.write(json_object)
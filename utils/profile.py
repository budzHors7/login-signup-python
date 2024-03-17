import json

def profile():
    print("profile")

def checkDetails():
    f = open("./tokens/users.json", "r")
    data = json.load(f)

    for i in data['users']:
        print(i)
    
    f.close()
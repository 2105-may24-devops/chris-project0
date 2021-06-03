#def welcome():
    #start = input('Welcome to your personal expense tracker. \nPlease type one of the following commands:\n'
                 # 'New\nRecord\nReview\nExit\n')


#def new_user():
    #balance = input('What is your monthly income?: ')
    #with open('archive.txt', 'w') as archive_file:
        #archive_file.write(balance)
    #input(f'Your balance is ${balance}, what would you like to do next?')


#def review():
    #balance = 0
    #item = ''
   # last_transaction = 0
    #input(f'Your current balance is: ${balance}\n'
          #f'Last transaction: ${last_transaction} on {item}, what would you like to do next')


#def record():
    #print(str(input('Item:\n')))
import json

def login(usr):
    uN = input("Name: ")
    pW = input("Password: ")

    if uN in usr.keys():
        if pW == usr[uN]:
            print("Welcome back.")
        else:
            print("Incorrect password.")
            return False
    else:


    writeUsers(usr)
    return True

def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def writeUsers(usr):
    with open("users.json", "w+") as f:
            json.dump(usr, f)

users = readUsers()
success = login(users)

while not success:
    success = login(users)
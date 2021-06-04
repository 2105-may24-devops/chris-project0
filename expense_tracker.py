
startup = ''
balance = 0

# def read_users():
# try:
# with open("users.json", "r") as f:
# return json.load(f)
# except FileNotFoundError:
# return {}


users = ''


# def write_users(users):
   # with open("users.json", "w+") as f:
       # json.dump(users, f)


def login(username):
    username = input("Name: ")
    password = input("Password: ")

    # writing new user login information to external file
    with open('archive.txt', 'w+') as archive_file:
        archive_file.write(username)

    # reading existing user login information from file
   # with open('archive.txt', 'r') as archive_file:
       # archive_file.read(password)
# if username in users.keys():
# if password == users[username]:
           # print("Welcome back.")

       # else:

           # print("Incorrect password.")
    # startup = input('What would you like to do next?')
   # else:
       # print("Hello, new person.")
# users[username] = password
       # write_users(users)
        # balance = input('Enter your monthly Income:$ ')
        # startup = input(f'Your balance is {balance}, what would you like to do next? ')

# printing user option menu
startup = input('Welcome to Spend Patrol \nPlease type one of the following commands:\n'
                'Login\nRecord\nReview\nExit\n')

while startup.lower() != 'exit':

    if startup.lower() == 'login':
        login(users)
        balance = input('Enter your balance')

        # balance = input('Enter your monthly Income:$ ')
        # startup = input(f'Your balance is {balance}, what would you like to do next? ')
        # archive_file = open archive.txt
    # with open('recording.txt', 'w') as archive_file:
    # archive_file.write(balance)
    # startup = input(f'Your balance is {balance}, what would you like to do next? ')

    # option to add new item to inventory
    elif startup.lower() == 'record':
        i = input('Item: ')
        p = input('\nPrice:$')
        balance_update = int(balance) - int(p)

        # updating inventory with new item and displaying current balance to user
        # with open('recording.txt', 'w') as archive_file:
        # archive_file.write(str(balance_update))
        print(f'Your new monthly balance is: ${balance_update}')
        

    elif startup.lower() == 'review':
        last_transaction = p
        item = i
        print(f'Your current balance is: ${balance_update}\n'
              f'Last transaction: ${last_transaction} on {item} ')
        # with open('recording.txt', 'a') as archive_file:
        # archive_file.write(last_transaction)

    elif startup.lower() == 'exit':
        print('Program exited')


    # while startup.lower() != 'exit' or 'new' or 'review' or 'record':
    else:
        print('Unrecognized command.')
    startup = input('Please type one of the following commands:\n'
                    'Login\nRecord\nReview\nExit\n')

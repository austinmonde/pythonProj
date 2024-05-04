pwd = input("What is the master password?: ")

def view():
    pass

#this function will create and add a new password into the file
def add():
    name = input('Account name: ')
    pwd = input('Password: ')

#the with key word will automatically close the file after use.
#the next parameter is the mode for opening the file: 
#(write: creates new or overides), (read: reads only existing ) and (append: adds to existing)
    with open('password.txt', 'a') as f: 




while True:
    mode = input("Would you like to enter a new password or view existing ones(view / add), press q to quit: ").lower()
    if mode =="q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue
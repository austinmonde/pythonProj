from cryptography.fernet import Fernet

pwd = input("What is the master password?: ")

#the with key word (with) automatically closes the file after use.
#the second parameter is the mode for opening the file: 
#(write: creates new or overides), (read: reads only existing) and (append: adds to existing)

#this function will only read the password.txt file
def view():
    with open('password.txt', 'r') as f: #f is the name of the file
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("|")
            print("User:", user, "| password:", passw)


#this function will create and add a new password into the file
def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f: #f is the name of the file
        f.write(name + "|" + pwd + "\n")

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
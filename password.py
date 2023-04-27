import string
import random 
import re # module for regular expression
import os
import hashlib
import getpass

# function for generating random alphanumeric strings for password
def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

# function to generate password  
def create_pass():
    print("Please insert the name of the website and the length of the password you would like to generate")
    website = input("Website name: ")
    size = int(input("Password length: "))
    while size < 8:
        print("please specify a better length for your password\nHint: anything more than 8 characters is preferred.")
        size = int(input("Password length: "))
    password = generate_password(size)
    
    with open('passwords.bin', 'ab') as f: # create password as binary
        f.write((website + '-' + password + "\n").encode()) # encode is used for binary string formatting
    os.system("attrib +h passwords.bin") # hides the file that contains the binary info of the created password
    print(f"The password for {website} is: {password}\n")

def prompt():
    query = int(input("Select:\n1. get password for a particular website\n2. list all the websites with passwords \n3. Exit\n"))
    return query

# function to help get the passwords of previously stored passwords
def password_query():
    print("Select an option after inserting your master password")
    verify = False # variable to keep track of the state of the program
    while verify == False:
        if 'ini.bin' in os.listdir(os.getcwd()):
            master_pass = getpass.getpass(prompt="Master password: ", stream=None)
            hashed_password = hashlib.sha256(master_pass.encode()).hexdigest()
            with open('pass.bin','rb') as f:
                data = f.readline().decode()
                if data == hashed_password:
                    print("welcome!")
                    verify = True
                else:
                    print("wrong master password. Please try again")
        else:
            print("Insert and remember your master password, as it would come in handy later on")
            init = ['ini','pass']
            for ini in init:
                with open(f'{ini}.bin','wb') as f:
                    if ini == 'pass':
                        master = input("Please insert your unique master password: ")
                        hash_function = hashlib.sha256(master.encode()).hexdigest()
                        f.write(hash_function.encode())
                os.system(f"attrib +h {ini}.bin")
            os.system("cls")

    print("Which of the following options would you select?")
    with open('passwords.bin','rb') as f:
        data = f.read().decode()
        weblist = re.findall(r"(\w*)-",data) # using regex to get the website names from our bin file.
    query = prompt()
    while query != 3:
        if query == 1:
            website = input("Website name: ")
            matches = re.findall(r"{}-(.*)".format(website),data) # using regex to get the websitre passwords from our bin file.
            for match in matches:
                print(match)
            print("\n")
            query = prompt()
        if query == 2:
            for web in weblist:
                print(web)
            print("\n")
            query = prompt()

if __name__ == "__main__":
    while True:
        try:
            option = int(input("Please choose an option \n1. Create new password\n2. Request a password\n3. Quit\n"))
            if option == 1:
                create_pass()
            if option == 2:
                password_query()
            if option == 3:
                break
        except ValueError:
            print("Please insert only numbers")
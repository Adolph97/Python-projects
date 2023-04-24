import string 
import random 
import re

def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))
    
def prompt():
    website = input("Please insert the name of the website you would like to generate a password for: ")
    size = int(input("Please specify the length of your password: "))
    while size < 8:
        print("please specify a better length for your password")
        size = int(input("Please specify the length of your password: "))
    password = generate_password(size)
    
    with open('passwords.bin', 'ab') as f:
        f.write((website + '-' + password + "\n").encode())

def readlines():
    master_pass = input("Please input masterpassword: ")
    if master_pass == "hey123":
        website = input("please specify a website you would like to query: ")
        with open('passwords.bin','rb') as f:
            data = f.read().decode()
            matches = re.findall(r"{}-(.*)".format(website),data)
        for match in matches:
            print(match)
    else:
        print("Please enter a correct password!")

while True:
    option = int(input("Please choose an option \n1. Create new password\n2. Read a particular password\n3. Quit\n"))

    if option == 1:
        prompt()
    if option == 2:
        readlines()
    if option == 3:
        break


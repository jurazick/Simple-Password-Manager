from cryptography.fernet import Fernet
import os.path


def write_key(k):
    key = 0
    if k:
        key = k
    else:
        key  = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read() 
    file.close
    return key

if os.path.getsize("key.key") <= 0:
    if input("Do you have a key? y/n: ").lower() == "n":
        write_key(False)
        print("Generated a new key keep it in a safe place")
    else:
        write_key(input("Paste your key here: ").encode())

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            label, user, pwd = data.split("|")
            print(label, "=> User:", fer.decrypt(user.encode()).decode(), "| Password:", 
                  fer.decrypt(pwd.encode()).decode())

def add():
    label = input("Login Label: ")
    user = input("Username: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(label + "|" + fer.encrypt(user.encode()).decode() + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Do you want to view logins or add a new login? (q to quit): ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
        continue
    if mode == "add":
        add()
        continue

    else:
        print("Invalid mode")
        continue

print("Make sure key.key is empty and keep your key in a safe place")
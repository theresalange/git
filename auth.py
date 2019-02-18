import getpass
import pickle
import random
import string

CHARS = string.ascii_letters + string.digits + string.punctuation

def hash_pwd(password):
    hashpwd = 0
    for char in password:
        hashpwd += ord(char)
    return hashpwd

def get_salt():
    salt_chars = random.choices(CHARS, k=10)
    salt = ''.join(salt_chars)
    return salt

def get_credentials():
    username = input("Enter username:")
    password = getpass.getpass("Enter password:")
    return (username, password)

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        if hash_pwd(password+pwdb[username][1]) == pwdb[username][0]:
            status = True
        else:
            print('Wrong password!')
    else:
        add_user(username, password, pwdb)

    return status

def add_user(username, password, pwdb):
    salt = get_salt()
    salted = password + salt
    hashed = hash_pwd(salted)
    pwdb[username] = (hashed, salt)
    write_pwdb(pwdb)

def read_pwdb():
    try:
        with open("pwdb.pkl", "rb") as fh:
            pwdb = pickle.load(fh)
    except FileNotFoundError:
        pwdb = {}

    return pwdb

def write_pwdb(pwdb):
    with open("pwdb.pkl", "wb") as fh:
        pickle.dump(pwdb, fh)


if __name__ == "__main__":
    username, password = get_credentials()
    pwdb = read_pwdb()
    status = authenticate(username, password, pwdb)
    if status:
        print('Authentication succeeded:', pwdb)
    else:
        print('Authentication failed')

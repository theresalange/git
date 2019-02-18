import getpass
import pickle

def pwhash(password):
    hashedpw = 0
    for char in password:
        hashedpw += ord(char)
    return hashedpw

def get_credentials():
    username = input("Enter username:")
    password = pwhash(getpass.getpass("Enter password:"))
    return (username, password)

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        if password == pwdb[username]:
            status = True
        else:
            print('Wrong password!')
    else:
        add_user(username, password, pwdb)

    return status

def add_user(username, password, pwdb):
    pwdb[username] = password
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

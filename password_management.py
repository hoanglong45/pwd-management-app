from cryptography.fernet import Fernet

root_pwd = 'qwe'

'''Generate key'''
# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key() + root_pwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username, password = data.split('|')
            print(f'Username: {username}')
            print(f'Password: {fer.decrypt(password.encode()).decode()}')            

def add():
    name = input('Username: ')
    pwd = input('Your password: ')

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')
    print('Add successfully')

def check_root_pwd(pwd):
    if pwd == root_pwd:
        return True
    else:
        return False

def pwd_management_app():
    while True:
        print('Please choose mode')
        print('1. view')
        print('2. add')
        print('3. quit')
        mode = int(input('Enter your mode: '))

        if mode == 1:
            view()
        elif mode == 2:
            add()
        elif mode == 3:
            break
        else:
            print('Invalid mode.')

def main():
    while True:
        print('PASSWORD MANAGEMENT APP')
        print('-----------------------')
        print('1. Access')
        print('2. Quit')
        mode = int(input('Enter your mode: '))

        if mode == 1:
            enter_root_pwd = input('What is your root password: ')
            if check_root_pwd(enter_root_pwd):
                pwd_management_app()
            else:
                print('Incorrect. Please enter your password again!')
        elif mode == 2:
            break
        else:
            print('Invalid mode.')

if __name__ == '__main__':
    main()
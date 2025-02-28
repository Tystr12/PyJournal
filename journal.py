# Program that I can use as a journal
# Password protected
# Commit comment to test commits

from dotenv import load_dotenv, set_key
import getpass
import os

DOTENV_PATH = r"C:\Users\Megam\Documents\realpython\running_scripts\j\.env"
load_dotenv() # load environment variables
my_password = os.getenv('TOKEN')
name = os.getenv("NAME")

def update_env_variable(key: str, value: str):
    """
    Update the environment variable in the running process AND
    persist it back into the .env file.
    """
    # Update in-memory environment (so other code can see the change right away)
    os.environ[key] = value
    
    # Persist the change back to the .env file
    set_key(DOTENV_PATH, key, value)


def show_all_options():
    show_options()
    print('5) -----Change password-----')
    print('6) -----Change name-----')

def change_name() -> None:
    '''Changes the name in the .env file (if i can figure this out)'''
    password = getpass.getpass("Enter your password: ")
    if(check_password(password)):
        new_name = input('Enter your name: ')
        update_env_variable("NAME", new_name)


def show_options() -> None:
    '''Prints the options the user has once logged in to the diary.'''
    print('1) -----Enter new log entry-----')
    print('2) -----Read previous logs-----')
    print('3) -----Exit-----')
    print('4) -----Help-----')



def print_starting_message() -> None:
    '''Prints starting message once logged in to the program with the user's name.'''
    print('**************************\n' +
          f"-------{name}'s Journal------- \n" +
          '**************************\n')


def check_password(password: str) -> bool:
    '''Checks if the password given in the parameter is the same that is saved in the .env file returns a boolean.'''

    if password == my_password:
        print('Correct Password! Access Granted!')
        return True
    else:
        return False


def change_password() -> None:
    '''Changes the current password if the user can verify the current password.'''
    current: str = getpass.getpass("Enter your current password: ")
    if(check_password(current) == True):
        new_password: str = getpass.getpass("Enter your new password: ")
        again: str = getpass.getpass("Enter your new password again: ")
        if new_password == again:
            update_env_variable("TOKEN", new_password)
            print("password is now changed!")
        else:
            print('passwords did not match! Try again.')
    else:
        print("password was not changed.. try again..")


def create_new_entry(title: str, content: str, date: str):
    '''Creates a new diary entry and saves it to the text file.'''
    text_file = open("something.txt", "a")
    text_file.write('------------------------------------\n')
    text_file.write(f'{title}\n')
    text_file.write(f' date: {date}\n')
    text_file.write(f'{content}\n')
    text_file.write('------------------------------------\n')
    text_file.close()


def read_the_diary():
    '''Loops over the entries in the diary and displays prints them to the console.'''
    text_file = open("something.txt", "r")
    data = text_file.read().splitlines()
    for line in data:
        print(line)


def save_entry_num() -> None:
    '''Increments the amount of entries that are in the diary when a new entry is created.'''
    text_file = open("saves.txt", "r")
    data = text_file.read()
    current_num = int(data[0])
    text_file = open("saves.txt", "w")
    res = current_num + 1
    text_file.write(str(res))
    text_file.close()


def show_num_of_entrys() -> None:
    '''Prints the amount of entries that are in the diary.'''
    text_file = open("saves.txt", "r")
    data = text_file.read()
    print(f'Number of entries: {data}')


enter_password = getpass.getpass("Enter your password: ")
if check_password(enter_password) == True:
    print_starting_message()
    running = True
    show_options()
    print('What would you like to do?')
else:
    print('Incorrect password. Try again...')

while(running == True):
    choice = input()
    if choice == 'new entry' or choice == '1':
        title = input('Title?\n')
        content = input('Write what you want to log\n')
        date = input('What is the date?\n')
        create_new_entry(title, content, date)
        save_entry_num()
        show_options()
    if choice == 'read prev' or choice == '2':
        read_the_diary()
        show_num_of_entrys()
        show_options()
    if choice == 'change password' == '5':
        password = input('enter current password')
        new_password = input('enter new password')
        change_password(password, new_password)
        show_options()
    if choice == 'change name':
        change_name()
        show_options()
    if choice == 'exit' or choice == '3':
        print("Closing journal...")
        running = False
    if choice == 'help' or choice == '4':
        show_all_options()
    if choice == 'change name' or choice == '6':
        change_name()
        show_options()

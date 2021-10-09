# Program that I can use as a journal
# Password protected
# Commit comment to test commits

from dotenv import load_dotenv
import os

load_dotenv()
my_password = os.getenv('TOKEN')

name = os.getenv("NAME")


def change_name() -> None:
    '''Changes the name in the .env file (if i can figure this out)'''
    password = input('Enter password to change your name')
    if(check_password(password)):
        new_name = input('Enter your name:')
        os.environ["NAME"] = new_name


def show_options() -> None:
    '''Prints the options the user has once logged in to the diary.'''
    print('1) -----Enter new log entry-----')
    print('2) -----Read previous logs-----')
    print('3) -----Exit-----')


def print_starting_message() -> None:
    '''Prints starting message once logged in to the program with the user's name.'''
    print('**************************\n' +
          f"-------{name}'s Journal------- \n" +
          '**************************\n')


def check_password(password: str) -> bool:
    '''Checks if the password given in the parameter is the same that is saved in the .env file returns a boolean.'''

    if password == my_password:
        return True
        print('Correct Password! Access Granted!')
    else:
        return False


def change_password(password: str, new_password: str) -> None:
    '''Changes the current password if the user can verify the current password.'''

    if(check_password(password) == True):
        my_password = new_password
        print("password is now changed!")
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


enter_password = input('Whats the password?')
if check_password(enter_password) == True:
    print_starting_message()
    running = True
    show_options()
    print('What would you like to do?')
else:
    print('Incorrect password. Try again...')

while(running == True):
    choice = input()
    if choice == 'new entry':
        title = input('Title?\n')
        content = input('Write what you want to log\n')
        date = input('What is the date?\n')
        create_new_entry(title, content, date)
        save_entry_num()
        show_options()
    if choice == 'read prev':
        read_the_diary()
        show_num_of_entrys()
        show_options()
    if choice == 'change password':
        password = input('enter current password')
        new_password = input('enter new password')
        change_password(password, new_password)
        show_options()
    if choice == 'change name':
        change_name()
        show_options()
    if choice == 'exit':
        running = False

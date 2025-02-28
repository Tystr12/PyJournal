import os
import getpass
from dotenv import load_dotenv, set_key
import bcrypt

DOTENV_PATH = r"C:\Users\Megam\Documents\realpython\running_scripts\j\.env"
load_dotenv(DOTENV_PATH)

my_password = os.getenv('TOKEN')
name = os.getenv('NAME')

def update_env_variable(key: str, value: str):
    os.environ[key] = value
    set_key(DOTENV_PATH, key, value)

def check_password(user_input: str) -> bool:
    """
    Compare the user's plain-text password with the hashed password in .env
    using passlib's bcrypt.verify.
    """
    if not my_password:
        print("No hashed password found in .env. Set TOKEN first.")
        return False
    # bcrypt.verify returns True or False
    return bcrypt.checkpw(user_input.encode(), my_password.encode())

def change_password():
    """
    Prompts for current password, and if verified, sets a new password
    hashed with passlib's bcrypt.
    """
    current = getpass.getpass("Enter your current password: ")
    if check_password(current):
        new_password = getpass.getpass("Enter your new password: ")
        again = getpass.getpass("Enter your new password again: ")
        if new_password == again:
            # Hash the new password using passlib's bcrypt
            hashed_str = bcrypt.hashpw(new_password)
            update_env_variable("TOKEN", hashed_str)
            print("Password is now changed and hashed!")
        else:
            print("Passwords did not match! Try again.")
    else:
        print("Password not changed.")

def change_name():
    """
    Prompt the user for current password, then change the NAME variable in .env.
    """
    password = getpass.getpass("Enter your password: ")
    if check_password(password):
        new_name = input('Enter your new name: ')
        update_env_variable("NAME", new_name)
        print(f"Name changed to: {new_name}")
    else:
        print("Name not changed.")

def print_starting_message():
    display_name = name if name else "User"
    print('**************************')
    print(f"-------{display_name}'s Journal-------")
    print('**************************\n')

def show_options():
    print('1) -----Enter new log entry-----')
    print('2) -----Read previous logs-----')
    print('3) -----Exit-----')
    print('4) -----Help-----')

def show_all_options():
    show_options()
    print('5) -----Change password-----')
    print('6) -----Change name-----')

def create_new_entry(title: str, content: str, date: str):
    with open("something.txt", "a", encoding="utf-8") as text_file:
        text_file.write('------------------------------------\n')
        text_file.write(f'{title}\n')
        text_file.write(f'date: {date}\n')
        text_file.write(f'{content}\n')
        text_file.write('------------------------------------\n')
    print("New entry saved!")

def read_the_diary():
    if not os.path.isfile("something.txt"):
        print("No diary entries yet. 'something.txt' not found.")
        return

    with open("something.txt", "r", encoding="utf-8") as text_file:
        data = text_file.read().splitlines()
        for line in data:
            print(line)

def save_entry_num():
    if not os.path.isfile("saves.txt"):
        with open("saves.txt", "w") as f:
            f.write("0")

    with open("saves.txt", "r") as text_file:
        data = text_file.read().strip()
        try:
            current_num = int(data)
        except ValueError:
            current_num = 0

    with open("saves.txt", "w") as text_file:
        res = current_num + 1
        text_file.write(str(res))

def show_num_of_entries():
    if not os.path.isfile("saves.txt"):
        print("Number of entries: 0")
        return

    with open("saves.txt", "r") as text_file:
        data = text_file.read().strip()
        print(f'Number of entries: {data or "0"}')

def main():
    if not my_password:
        print("No TOKEN set in .env! Please set TOKEN in your .env file (hashed or blank).")
        return

    password_attempt = getpass.getpass("Enter your password: ")
    if not check_password(password_attempt):
        return  # Exit if incorrect

    print_starting_message()
    running = True
    show_options()
    print('What would you like to do?')

    while running:
        choice = input("> ").strip().lower()

        if choice in ('1', 'new entry'):
            title = input('Title?\n')
            content = input('Write what you want to log\n')
            date = input('What is the date?\n')
            create_new_entry(title, content, date)
            save_entry_num()
            show_options()

        elif choice in ('2', 'read prev'):
            read_the_diary()
            show_num_of_entries()
            show_options()

        elif choice in ('3', 'exit'):
            print("Closing journal...")
            running = False

        elif choice in ('4', 'help'):
            show_all_options()

        elif choice in ('5', 'change password'):
            change_password()
            show_options()

        elif choice in ('6', 'change name'):
            change_name()
            show_options()

        else:
            print("Invalid choice. Try again or type 'help' for options.")

if __name__ == "__main__":
    main()

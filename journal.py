import os
import getpass
from dotenv import load_dotenv, set_key

# Path to your .env file (adjust as needed)
DOTENV_PATH = r"C:\Users\Megam\Documents\realpython\running_scripts\j\.env"

# Load environment variables
load_dotenv(DOTENV_PATH)

# Retrieve variables from .env (if they exist)
my_password = os.getenv('TOKEN')
name = os.getenv("NAME")


def update_env_variable(key: str, value: str):
    """
    Update an environment variable both in memory and in the .env file.
    """
    os.environ[key] = value
    set_key(DOTENV_PATH, key, value)


def check_password(password: str) -> bool:
    """
    Check if the user-inputted password matches the one stored in .env.
    """
    if password == my_password:
        print('Correct Password! Access Granted!')
        return True
    else:
        print('Incorrect password!')
        return False


def show_options() -> None:
    """
    Print the options available to the user once logged in.
    """
    print('1) -----Enter new log entry-----')
    print('2) -----Read previous logs-----')
    print('3) -----Exit-----')
    print('4) -----Help-----')


def show_all_options() -> None:
    """
    Show the full options list (including changing name/password).
    """
    show_options()
    print('5) -----Change password-----')
    print('6) -----Change name-----')


def print_starting_message() -> None:
    """
    Print a welcome banner showing the current user’s name from .env.
    """
    # Fallback if NAME isn't set
    display_name = name if name else "User"
    print('**************************')
    print(f"-------{display_name}'s Journal-------")
    print('**************************\n')


def create_new_entry(title: str, content: str, date: str):
    """
    Create a new journal entry and append it to the 'something.txt' file.
    """
    # Safely open the file with a 'with' statement
    with open("something.txt", "a", encoding="utf-8") as text_file:
        text_file.write('------------------------------------\n')
        text_file.write(f'{title}\n')
        text_file.write(f'date: {date}\n')
        text_file.write(f'{content}\n')
        text_file.write('------------------------------------\n')
    print("New entry saved!")


def read_the_diary():
    """
    Print out all entries from 'something.txt'.
    """
    if not os.path.isfile("something.txt"):
        print("No diary entries yet. 'something.txt' not found.")
        return

    with open("something.txt", "r", encoding="utf-8") as text_file:
        data = text_file.read().splitlines()
        for line in data:
            print(line)


def save_entry_num() -> None:
    """
    Increments the count of entries stored in 'saves.txt' (used for tracking entry number).
    """
    # If the saves.txt file doesn't exist, create it with an initial '0'.
    if not os.path.isfile("saves.txt"):
        with open("saves.txt", "w") as f:
            f.write("0")

    with open("saves.txt", "r") as text_file:
        data = text_file.read().strip()

        # Safely convert to int (fallback to 0 if empty)
        try:
            current_num = int(data)
        except ValueError:
            current_num = 0

    with open("saves.txt", "w") as text_file:
        res = current_num + 1
        text_file.write(str(res))


def show_num_of_entries() -> None:
    """
    Print the number of entries stored in 'saves.txt'.
    """
    if not os.path.isfile("saves.txt"):
        print("Number of entries: 0")
        return

    with open("saves.txt", "r") as text_file:
        data = text_file.read().strip()
        print(f'Number of entries: {data or "0"}')


def change_name() -> None:
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


def change_password() -> None:
    """
    Prompt user for current password, confirm, then change the TOKEN variable in .env.
    """
    current = getpass.getpass("Enter your current password: ")
    if check_password(current):
        new_password = getpass.getpass("Enter your new password: ")
        again = getpass.getpass("Enter your new password again: ")
        if new_password == again:
            update_env_variable("TOKEN", new_password)
            print("Password is now changed!")
        else:
            print("Passwords did not match! Try again.")
    else:
        print("Password not changed.")


def main():
    """
    Main function: prompt for password, then let the user choose what to do.
    """
    # If there's no TOKEN in .env, warn user or prompt them to create one
    if not my_password:
        print("No TOKEN set in .env! Please set TOKEN=somepassword in your .env file.")
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

'''
    Written by Ty Strong
    Last updated: 28.02.2025
'''

import os
import getpass
from dotenv import load_dotenv, set_key
import bcrypt
from rich.console import Console
from cryptography.fernet import Fernet

DOTENV_PATH = r"C:\Users\Megam\Documents\realpython\running_scripts\j\.env"
load_dotenv(DOTENV_PATH)

console = Console()
my_password = os.getenv('TOKEN')
name = os.getenv('NAME')
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is missing! Please set it in .env.")

cipher = Fernet(SECRET_KEY.encode())

def encrypt_message(message: str) -> str:
    """Encrypts a message using Fernet encryption."""
    encrypted_text = cipher.encrypt(message.encode())
    return encrypted_text.decode()  # Convert bytes to string for storage

def decrypt_message(encrypted_message: str) -> str:
    """Decrypts an encrypted message using Fernet encryption."""
    decrypted_text = cipher.decrypt(encrypted_message.encode())
    return decrypted_text.decode()

def print(output: str) -> None:
    console.print(output)

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
    print("[bold red]Enter your current password: [/bold red]")
    current = getpass.getpass()
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
    print("[bold red]Enter your password: [/bold red]")
    password = getpass.getpass()
    if check_password(password):
        new_name = input('Enter your new name: ')
        update_env_variable("NAME", new_name)
        print(f"[bold green]Name changed to: {new_name}[/bold green]")
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
    encrypted_title = encrypt_message(title)
    encrypted_content = encrypt_message(content)
    encrypted_date = encrypt_message(date)

    with open("something.txt", "a", encoding="utf-8") as text_file:
        text_file.write('------------------------------------\n')
        text_file.write(f'Title: {encrypted_title}\n')
        text_file.write(f'Date: {encrypted_date}\n')
        text_file.write(f'Content: {encrypted_content}\n')
        text_file.write('------------------------------------\n')
    print("[bold green]New entry saved![/bold green]")

def read_the_diary():
    """Reads and decrypts all journal entries."""
    if not os.path.isfile("something.txt"):
        print("No journal entries found.")
        return

    with open("something.txt", "r", encoding="utf-8") as text_file:
        data = text_file.read().splitlines()

    decrypted_entries = []
    for line in data:
        if line.startswith("Title: "):
            decrypted_entries.append("Title: " + decrypt_message(line[7:]))
        elif line.startswith("Date: "):
            decrypted_entries.append("Date: " + decrypt_message(line[6:]))
        elif line.startswith("Content: "):
            decrypted_entries.append("Content: " + decrypt_message(line[9:]))
        else:
            decrypted_entries.append(line)  # Keep dividers as they are

    # Print decrypted entries
    for line in decrypted_entries:
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

    print("[bold red]Enter your password: [/bold red]")
    password_attempt = getpass.getpass()
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
            print("[bold blue]Closing journal...[/bold blue]")
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

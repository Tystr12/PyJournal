# PyJournal

A lightweight, password-protected, **terminal-based journaling application** written in Python. Perfect for quickly jotting down personal notes or diaries securely in a local environment.

## Features

- **Password-Protected**:
  - Uses **bcrypt** to store your password in a hashed form in the `.env` file.
  - During login, your input is hashed and compared to the stored hash for verification.
- **Simple Text Logs**: Entries are appended to a simple `.txt` file.
- **Entry Counter**: Automatically tracks the total number of journal entries in `saves.txt`.
- **Change Password/Name**: Update your hashed password (`TOKEN`) or the `NAME` used in banners.

## Requirements

1. **Python 3.7+** (recommended)
2. **python-dotenv** for reading and writing environment variables.  
3. **bcrypt** for password hashing increasing security. 
4. **cryptography** for secure storage of journal entries

Use requirements.txt to install all dependencies to run PyJournal.

```bash
# Create a virtual environment
python -m venv my_venv

# Activate the virtual environment (Windows)
my_venv\Scripts\activate

# Activate on Mac/Linux
source my_venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Terminal Journal

A lightweight, password-protected, **terminal-based journaling application** written in Python. Perfect for quickly jotting down personal notes or diaries securely in a local environment.

## Features

- **Password-Protected**: Ensures only the correct user can access and modify entries.
- **Simple Text Logs**: Entries are appended to a simple `.txt` file.
- **Entry Counter**: Automatically tracks the total number of journal entries in `saves.txt`.
- **Change Password/Name**: Update the stored `TOKEN` (password) or the `NAME` used in banners.

## Requirements

1. **Python 3.7+** (recommended)
2. **python-dotenv** for reading and writing environment variables.  
   Install with:
   ```bash
   pip install python-dotenv

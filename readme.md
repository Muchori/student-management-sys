# Student Management System (ID: 1731)

This is a secure student management system implemented in Python. It features a SQLite database with encryption, a GUI built with Tkinter, and includes a secure calculator utility.

## Project Structure

- `src/`: Contains the source code
  - `database/`: Database-related code
  - `gui/`: GUI-related code
  - `utils/`: Utility classes and functions
- `tests/`: Contains unit tests
- `requirements.txt`: List of Python package dependencies
- `run.py`: Entry point for running the application

## Installation and Setup

### Windows

1. Install Python:

   - Download Python from [python.org](https://www.python.org/downloads/windows/)
   - During installation, ensure you check "Add Python to PATH"

2. Clone the repository:

   ```
   git clone https://github.com/yourusername/student-management-system-1731.git
   cd student-management-system-1731
   ```

3. (Optional) Create a virtual environment:

   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Install required packages:

   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python run.py
   ```

### Linux-based Systems (Ubuntu/Debian example)

1. Install Python and required system packages:

   ```
   sudo apt update
   sudo apt install python3 python3-pip python3-venv python3-tk
   ```

2. Clone the repository:

   ```
   git clone https://github.com/yourusername/student-management-sys.git
   cd student-management-sys
   ```

3. (Optional) Create a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install required packages:

   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python run.py
   ```

## Running Tests

To run the unit tests:

### Windows

```
python -m unittest discover tests
```

### Linux

```
python3 -m unittest discover tests
```

## Troubleshooting

### Windows

- If Python is not recognized, ensure it's added to your PATH environment variable.
- For Tkinter issues, reinstall Python and make sure to check "tcl/tk and IDLE" during installation.

### Linux

- If you encounter a "no module named tkinter" error, install the python3-tk package:
  ```
  sudo apt install python3-tk
  ```
- If `python` command is not found, try using `python3` instead.

## Additional Notes

- Ensure you have the necessary permissions to write to the directory where the database file will be created.
- For any "DLL load failed" errors on Windows, ensure all required Visual C++ redistributables are installed.

## Author

Student ID: 1731

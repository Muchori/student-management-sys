import sys
import os
import tkinter as tk

# Get the parent directory of the current file (which is the 'src' folder)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database.database import Database
from src.gui.gui import GUI

def main():
    db = Database('student_management_system_1731.sqlite')
    root = tk.Tk()
    app = GUI(root, db)
    root.mainloop()
    db.close()

if __name__ == "__main__":
    main()

from secure_database import SecureDatabase
from gui import GUI

def main():
    db = SecureDatabase('student_management_system_1731.sqlite')
    root = tk.Tk()
    app = GUI(root, db)
    root.mainloop()
    db.close()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import ttk, messagebox
from src.database.database import Database
from src.utils.calculator import Calculator

class GUI:
    def __init__(self, master, db):
        self.master = master
        self.db = db
        self.master.title("Student Management System - 1731")
        self.master.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=1, fill="both")

        self.students_tab = ttk.Frame(self.notebook)
        self.courses_tab = ttk.Frame(self.notebook)
        self.instructors_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.students_tab, text="Students")
        self.notebook.add(self.courses_tab, text="Courses")
        self.notebook.add(self.instructors_tab, text="Instructors")

        self.setup_students_tab()
        self.setup_courses_tab()
        self.setup_instructors_tab()

    def setup_students_tab(self):
        student_notebook = ttk.Notebook(self.students_tab)
        student_notebook.pack(expand=1, fill="both")

        add_student_tab = ttk.Frame(student_notebook)
        view_students_tab = ttk.Frame(student_notebook)

        student_notebook.add(add_student_tab, text="Add Student")
        student_notebook.add(view_students_tab, text="View Students")

        ttk.Label(add_student_tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.student_name_entry = ttk.Entry(add_student_tab)
        self.student_name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_student_tab, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        self.student_age_entry = ttk.Entry(add_student_tab)
        self.student_age_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_student_tab, text="Grade:").grid(row=2, column=0, padx=5, pady=5)
        self.student_grade_entry = ttk.Entry(add_student_tab)
        self.student_grade_entry.grid(row=2, column=1, padx=5, pady=5)

        self.student_consent_var = tk.BooleanVar()
        ttk.Checkbutton(add_student_tab, text="Privacy Consent", variable=self.student_consent_var).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        ttk.Button(add_student_tab, text="Add Student", command=self.add_student).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.students_tree = ttk.Treeview(view_students_tab, columns=("ID", "Name", "Age", "Grade", "Consent"), show="headings")
        self.students_tree.heading("ID", text="ID")
        self.students_tree.heading("Name", text="Name")
        self.students_tree.heading("Age", text="Age")
        self.students_tree.heading("Grade", text="Grade")
        self.students_tree.heading("Consent", text="Consent")
        self.students_tree.pack(padx=5, pady=5)

        ttk.Button(view_students_tab, text="Refresh", command=self.refresh_students).pack(padx=5, pady=5)

        self.refresh_students()

    def setup_courses_tab(self):
        course_notebook = ttk.Notebook(self.courses_tab)
        course_notebook.pack(expand=1, fill="both")

        add_course_tab = ttk.Frame(course_notebook)
        view_courses_tab = ttk.Frame(course_notebook)

        course_notebook.add(add_course_tab, text="Add Course")
        course_notebook.add(view_courses_tab, text="View Courses")

        ttk.Label(add_course_tab, text="Course Name:").grid(row=0, column=0, padx=5, pady=5)
        self.course_name_entry = ttk.Entry(add_course_tab)
        self.course_name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_course_tab, text="Course Code:").grid(row=1, column=0, padx=5, pady=5)
        self.course_code_entry = ttk.Entry(add_course_tab)
        self.course_code_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_course_tab, text="Instructor ID:").grid(row=2, column=0, padx=5, pady=5)
        self.course_instructor_entry = ttk.Entry(add_course_tab)
        self.course_instructor_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(add_course_tab, text="Add Course", command=self.add_course).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.courses_tree = ttk.Treeview(view_courses_tab, columns=("ID", "Name", "Code", "Instructor ID"), show="headings")
        self.courses_tree.heading("ID", text="ID")
        self.courses_tree.heading("Name", text="Name")
        self.courses_tree.heading("Code", text="Code")
        self.courses_tree.heading("Instructor ID", text="Instructor ID")
        self.courses_tree.pack(padx=5, pady=5)

        ttk.Button(view_courses_tab, text="Refresh", command=self.refresh_courses).pack(padx=5, pady=5)

        self.refresh_courses()

    def setup_instructors_tab(self):
        instructor_notebook = ttk.Notebook(self.instructors_tab)
        instructor_notebook.pack(expand=1, fill="both")

        add_instructor_tab = ttk.Frame(instructor_notebook)
        view_instructors_tab = ttk.Frame(instructor_notebook)

        instructor_notebook.add(add_instructor_tab, text="Add Instructor")
        instructor_notebook.add(view_instructors_tab, text="View Instructors")

        ttk.Label(add_instructor_tab, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.instructor_name_entry = ttk.Entry(add_instructor_tab)
        self.instructor_name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(add_instructor_tab, text="Department:").grid(row=1, column=0, padx=5, pady=5)
        self.instructor_department_entry = ttk.Entry(add_instructor_tab)
        self.instructor_department_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(add_instructor_tab, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.instructor_email_entry = ttk.Entry(add_instructor_tab)
        self.instructor_email_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(add_instructor_tab, text="Add Instructor", command=self.add_instructor).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.instructors_tree = ttk.Treeview(view_instructors_tab, columns=("ID", "Name", "Department", "Email"), show="headings")
        self.instructors_tree.heading("ID", text="ID")
        self.instructors_tree.heading("Name", text="Name")
        self.instructors_tree.heading("Department", text="Department")
        self.instructors_tree.heading("Email", text="Email")
        self.instructors_tree.pack(padx=5, pady=5)

        ttk.Button(view_instructors_tab, text="Refresh", command=self.refresh_instructors).pack(padx=5, pady=5)

        self.refresh_instructors()

    def add_student(self):
        name = self.student_name_entry.get()
        age = self.student_age_entry.get()
        grade = self.student_grade_entry.get()
        consent = self.student_consent_var.get()

        if name and age and grade:
            try:
                age = int(age)
                self.db.add_student(name, age, grade, consent)
                messagebox.showinfo("Success", "Student added successfully!")
                self.clear_student_entries()
                self.refresh_students()
            except ValueError:
                messagebox.showerror("Error", "Age must be a number!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def clear_student_entries(self):
        self.student_name_entry.delete(0, tk.END)
        self.student_age_entry.delete(0, tk.END)
        self.student_grade_entry.delete(0, tk.END)
        self.student_consent_var.set(False)

    def refresh_students(self):
        for i in self.students_tree.get_children():
            self.students_tree.delete(i)
        students = self.db.get_all_students()
        for student in students:
            self.students_tree.insert("", "end", values=student)

    def add_course(self):
        name = self.course_name_entry.get()
        code = self.course_code_entry.get()
        instructor_id = self.course_instructor_entry.get()

        if name and code and instructor_id:
            try:
                instructor_id = int(instructor_id)
                self.db.add_course(name, code, instructor_id)
                messagebox.showinfo("Success", "Course added successfully!")
                self.clear_course_entries()
                self.refresh_courses()
            except ValueError:
                messagebox.showerror("Error", "Instructor ID must be a number!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def clear_course_entries(self):
        self.course_name_entry.delete(0, tk.END)
        self.course_code_entry.delete(0, tk.END)
        self.course_instructor_entry.delete(0, tk.END)

    def refresh_courses(self):
        for i in self.courses_tree.get_children():
            self.courses_tree.delete(i)
        courses = self.db.get_all_courses()
        for course in courses:
            self.courses_tree.insert("", "end", values=course)

    def add_instructor(self):
        name = self.instructor_name_entry.get()
        department = self.instructor_department_entry.get()
        email = self.instructor_email_entry.get()

        if name and department and email:
            self.db.add_instructor(name, department, email)
            messagebox.showinfo("Success", "Instructor added successfully!")
            self.clear_instructor_entries()
            self.refresh_instructors()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def clear_instructor_entries(self):
        self.instructor_name_entry.delete(0, tk.END)
        self.instructor_department_entry.delete(0, tk.END)
        self.instructor_email_entry.delete(0, tk.END)

    def refresh_instructors(self):
        for i in self.instructors_tree.get_children():
            self.instructors_tree.delete(i)
        instructors = self.db.get_all_instructors()
        for instructor in instructors:
            self.instructors_tree.insert("", "end", values=instructor)
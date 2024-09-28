import unittest
from src.database.database import Database
import os

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test_database_1731.sqlite'
        self.db = Database(self.db_name)

    def tearDown(self):
        self.db.close()
        os.remove(self.db_name)

    def test_add_student_1731(self):
        self.db.add_student("John Doe", 20, "A", True)
        student = self.db.get_student(1)
        self.assertEqual(student[1], "John Doe")
        self.assertEqual(student[2], 20)
        self.assertEqual(student[3], "A")
        self.assertTrue(student[4])

    def test_add_course_1731(self):
        self.db.add_course("Mathematics", "MATH101", 1)
        course = self.db.get_course(1)
        self.assertEqual(course[1], "Mathematics")
        self.assertEqual(course[2], "MATH101")
        self.assertEqual(course[3], 1)

    def test_add_instructor_1731(self):
        self.db.add_instructor("Jane Smith", "Mathematics", "jane@example.com")
        instructor = self.db.get_instructor(1)
        self.assertEqual(instructor[1], "Jane Smith")
        self.assertEqual(instructor[2], "Mathematics")
        self.assertEqual(instructor[3], "jane@example.com")

    # Add more tests for update, delete, and get_all operations

if __name__ == '__main__':
    unittest.main()
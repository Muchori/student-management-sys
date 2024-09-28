import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333, places=6)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            self.calc.add("2", 3)
        with self.assertRaises(TypeError):
            self.calc.subtract(4, "2")
        with self.assertRaises(TypeError):
            self.calc.multiply("2", "3")
        with self.assertRaises(TypeError):
            self.calc.divide(6, "3")

if __name__ == '__main__':
    unittest.main()
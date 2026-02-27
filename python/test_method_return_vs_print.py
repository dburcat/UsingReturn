"""
Unit test for method_return_vs_print.py
"""

import unittest
from method_return_vs_print import (
    square, add_then_multiply, calculate_tax, 
    create_greeting, find_max
)


class TestMethodReturnVsPrint(unittest.TestCase):
    """
    Test the functions that return values from method_return_vs_print.py
    """
    
    def test_square(self):
        """Test the square function"""
        self.assertEqual(square(4), 16)
        self.assertEqual(square(0), 0)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(10), 100)
    
    def test_add_then_multiply(self):
        """Test the add_then_multiply function"""
        self.assertEqual(add_then_multiply(3, 4, 2), 14)
        self.assertEqual(add_then_multiply(1, 1, 5), 10)
        self.assertEqual(add_then_multiply(0, 5, 3), 15)
    
    def test_calculate_tax(self):
        """Test the calculate_tax function"""
        self.assertAlmostEqual(calculate_tax(100.0, 0.08), 8.0)
        self.assertAlmostEqual(calculate_tax(29.99, 0.08), 2.3992)
        self.assertEqual(calculate_tax(0, 0.1), 0)
    
    def test_create_greeting(self):
        """Test the create_greeting function"""
        self.assertEqual(create_greeting("Python"), "Hello, Python!")
        self.assertEqual(create_greeting("World"), "Hello, World!")
        self.assertEqual(create_greeting(""), "Hello, !")
    
    def test_find_max(self):
        """Test the find_max function"""
        self.assertEqual(find_max(10, 7, 15), 15)
        self.assertEqual(find_max(1, 2, 3), 3)
        self.assertEqual(find_max(5, 5, 5), 5)
        self.assertEqual(find_max(-1, -2, -3), -1)


if __name__ == '__main__':
    unittest.main()
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/mathematical_operations')))

from mathematical_operations import addition, subtraction, multiply, division
import unittest

class TestOperations(unittest.TestCase):
        def test_operations(self):
                self.assertEqual(addition(5, 3), 8)
                self.assertEqual(subtraction(5, 3), 2)
                self.assertEqual(multiply(5, 3), 15)

unittest.main()


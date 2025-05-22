import unittest
import os
import sys

# Add the parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tshirts_alternate import size

class TestTShirtSizing(unittest.TestCase):
    def test_small_size(self):
        self.assertEqual(size(37), 'S')

    def test_medium_size(self):
        self.assertEqual(size(40), 'M')

    def test_large_size(self):
        self.assertEqual(size(43), 'L')
        
    def test_boundary_case(self):
        self.assertEqual(size(42), 'L')
        self.assertEqual(size(38), 'M')
        self.assertEqual(size(38.5), 'M')
        self.assertEqual(size(30), 'S')
        self.assertEqual(size(50), 'L')
        self.assertEqual(size(50.1), 'Invalid')
        self.assertEqual(size(29.9), 'Invalid')

    def test_invalid_inputs(self):
        self.assertEqual(size(15), 'Invalid')
        self.assertEqual(size(60), 'Invalid')
        self.assertEqual(size(0), 'Invalid')
        self.assertEqual(size(-5), 'Invalid')
        self.assertEqual(size("abc"), 'Invalid')

if __name__ == '__main__':
    unittest.main() 
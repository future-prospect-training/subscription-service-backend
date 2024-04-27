import unittest

def add(num1, num2):
    return num1 + num2

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Test logic goes here
        self.assertEqual(1 + 1, 2)

    def test_add(self):
        result = add(5, 3)
        self.assertEqual(result, 4)
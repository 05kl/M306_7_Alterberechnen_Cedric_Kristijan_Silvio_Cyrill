import unittest
from alter_func import printAge

class TestPrintAge(unittest.TestCase):
    def test_yesterday_date(self):
        args = ["alter_func.py", "19.10.2025"]
        self.assertEqual(printAge(args), 0)
    def test_past_date(self):
        args = ["alter_func.py", "06.07.2012"]
        self.assertEqual(printAge(args), 0)
    def test_future_date(self):
        args = ["alter_func.py", "21.10.2025"]
        self.assertEqual(printAge(args), 1)
    def test_wrong_input(self):
        args = ["alter_func.py", "Hallo"]
        self.assertEqual(printAge(args), 1)
    def test_wrong_date(self):
        args = ["alter_func.py", "33.33.5000"]
        self.assertEqual(printAge(args), 1)

if __name__ == '__main__':
    unittest.main()

import unittest
from alter_func import printAge

class TestPrintAge(unittest.TestCase):
    def test_yesterday_date(self):
        args = ["alter_func.py", "19.10.2025"]
        self.assertEqual(printAge(args), 0)

if __name__ == '__main__':
    unittest.main()

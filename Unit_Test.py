import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)

if __name__ == '__main__':
    unittest.main()

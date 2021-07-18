import unittest
import calculator
    

class MyTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10,5), 15)
        self.assertEqual(calculator.add(-1,1), 0)
        self.assertEqual(calculator.add(-1,-1), -2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10,5), 5)
        self.assertEqual(calculator.subtract(-1,1), -2)
        self.assertEqual(calculator.subtract(-1,-1), 0)


    def test_multiple(self):
        self.assertEqual(calculator.multiple(10,5), 50)
        self.assertEqual(calculator.multiple(-1,1), -1)
        self.assertEqual(calculator.multiple(-1,-1), 1)

    def test_divide(self):
        self.assertEqual(calculator.divide(10,5), 2)
        self.assertEqual(calculator.divide(-1,1), -1)
        self.assertEqual(calculator.divide(-1,-1), 1)

        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
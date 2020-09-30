import unittest
from HW8 import *

class testFunctions(unittest.TestCase):

    def test_getDigits(self):
            self.assertEqual(getDigits(0), [0])
            self.assertEqual(getDigits(1), [1])
            self.assertEqual(getDigits(100), [1,0,0])
            self.assertEqual(getDigits(514), [5,1,4])

    def test_isMirrorMatch(self):
            self.assertEqual(isMirrorMatch(1,2,2,1), True)
            self.assertEqual(isMirrorMatch(0,0,0,0), True)
            self.assertEqual(isMirrorMatch(2,2,2,2), True)
            self.assertEqual(isMirrorMatch(6,9,6,9), False)

    def test_isDigitMatch(self):
            self.assertEqual(isDigitMatch(1,2,2,1), True)
            self.assertEqual(isDigitMatch(0,0,0,0), True)
            self.assertEqual(isDigitMatch(0,0,0,1), True)
            self.assertEqual(isDigitMatch(6,9,2,3), False)

    def test_winnings(self):
            self.assertEqual(winnings(69,69), 10000)
            self.assertEqual(winnings(15,51), 3000)
            self.assertEqual(winnings(69,39), 1000)
            self.assertEqual(winnings(69,41), 0)

if __name__ == '__main__':
    unittest.main()


from mySolution import generate, calcScore

import unittest

class generateTest(unittest.TestCase):
    def testZeroLength(self):
        data1 = 0
        data2 = 0
        data3 = ''
        result = generate(data1, data2, data3)
        self.assertEqual(result, [])

    def testGreaterThanZeroLength(self):
        data1 = 4
        data2 = 4
        data3 = 'abcd'
        resultLen = len(generate(data1, data2, data3))
        self.assertEqual(resultLen, 4)

class scoreTest(unittest.TestCase):

    def testEmptyString(self):
        data1 = ""
        data2 = "me t"
        result = calcScore(data1, data2)
        self.assertEqual(result, 0)

    def test50Percent(self):
        data1 = "meil"
        data2 = "me t"
        result = calcScore(data1, data2)
        self.assertEqual(result, 50)

    def test100Percent(self):
        data1 = "me t"
        data2 = "me t"
        result = calcScore(data1, data2)
        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
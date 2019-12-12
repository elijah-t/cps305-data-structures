from mySolution import power, powerH, C

import unittest

class powerTest(unittest.TestCase):
    
    def testZeroPower(self):
        data1, data2 = 4, 0
        result = power(data1, data2)
        self.assertEqual(result, 1)

    def testOnePower(self):
        data1, data2 = 3, 1
        result = power(data1, data2)
        self.assertEqual(result, 3)

    def testHighPower(self):
        data1, data2 = 2, 10
        result = power(data1, data2)
        self.assertEqual(result, 1024)

    def testZeroNumber(self):
        data1, data2 = 0, 4
        result = power(data1, data2)
        self.assertEqual(result, 0)

    def testHighNumber(self):
        data1, data2 = 10, 5
        result = power(data1, data2)
        self.assertEqual(result, 100000)

class powerHalveTest(unittest.TestCase):

    def testZeroPower(self):
        data1, data2 = 4, 0
        result = power(data1, data2)
        self.assertEqual(result, 1)

    def testOnePower(self):
        data1, data2 = 3, 1
        result = power(data1, data2)
        self.assertEqual(result, 3)

    def testHighPower(self):
        data1, data2 = 2, 10
        result = power(data1, data2)
        self.assertEqual(result, 1024)

    def testZeroNumber(self):
        data1, data2 = 0, 4
        result = power(data1, data2)
        self.assertEqual(result, 0)

    def testHighNumber(self):
        data1, data2 = 10, 5
        result = power(data1, data2)
        self.assertEqual(result, 100000)

class binomialDistribTest(unittest.TestCase):

    def testEqual(self):
        data1, data2 = 5, 5
        result = C(data1, data2)
        self.assertEqual(result, 1)

    def testKEqualsZero(self):
        data1, data2 = 4, 0
        result = C(data1, data2)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    

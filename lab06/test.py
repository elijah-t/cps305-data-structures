from sorting import mo3_quicksort

import unittest

class mo3QuicksortTest(unittest.TestCase):
    
    def testEmptyList(self):
        data = []
        mo3_quicksort(data)
        self.assertEqual(data, [])

    def testOneElement(self):
        data = [1]
        mo3_quicksort(data)
        self.assertEqual(data, [1])

    def testLargeList(self):
        data = [38, 27, 76, 90, 16, 74, 70, 88, 63]
        mo3_quicksort(data)
        self.assertEqual(data, [16, 27, 38, 63, 70, 74, 76, 88, 90])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
from myParser import parse

import unittest

class parseTest(unittest.TestCase):

    def testNum(self):
        data = ['1'] #1
        result = parse(data)
        self.assertEqual(['1', [], []], result)

    def testUnary(self):
        data = ['3', '!'] #3!
        result = parse(data)
        self.assertEqual(['!', ['3', [], []], []], result)

    def testBinary(self):
        data = ['2', '*', '9']
        result = parse(data)
        self.assertEqual(['*', ['2', [], []], ['9', [], []]], result)

    def testParenthesis(self):
        data = [['6', '-', '2'], '/', '8'] #(6-2)/8
        result = parse(data)
        self.assertEqual(['/', ['-', ['6', [], []], ['2', [], []]], ['8', [], []]], result)

    def testUnaryParenthesis(self):
        data = ['7', '*', ['3', '+', '4'], '!']
        result = parse(data)
        self.assertEqual(['*', ['7', [], []], ['!', ['+', ['3', [], []], ['4', [], []]], []]], result)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
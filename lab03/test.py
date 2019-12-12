from mySolution import infixToPostfixEval

import unittest

class converionEvalTest(unittest.TestCase):

    def testOneOperator(self):
        data = "1 + 1"
        result = infixToPostfixEval(data)
        self.assertEqual(result[0], "1 1 +")
        self.assertEqual(result[1], 2)
    
    def testTwoOperators(self):
        data = "1 + 2 * 3"
        result = infixToPostfixEval(data)
        self.assertEqual(result[0], "1 2 3 * +")
        self.assertEqual(result[1], 7)

    def testParenthesis(self):
        data = "( 5 + 9 ) * 7 + 2"
        result = infixToPostfixEval(data)
        self.assertEqual(result[0], "5 9 + 7 * 2 +")
        self.assertEqual(result[1], 100)

    def testFactorial(self):
        data = "5 ! + 3 * 7"
        result = infixToPostfixEval(data)
        self.assertEqual(result[0], "5 ! 3 7 * +")
        self.assertEqual(result[1], 141)
    
    def testLongExp(self):
        data = "( 9 + 3 ) / 6 * 7 - 2 ! * 4"
        result = infixToPostfixEval(data)
        self.assertEqual(result[0], "9 3 + 6 / 7 * 2 ! 4 * -")
        self.assertEqual(result[1], 6)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
from eval import evalTree

import unittest

class evalTreeTest(unittest.TestCase):

    def testRoot(self):
        data1 = ["30", [], []] #x=125,y=250,z=300; 30
        data2 = [["x", 125], ["y", 250], ["z", 300]]
        result = evalTree(data1, data2)
        self.assertEqual(30, result)

    def testEnvironment(self):
        data1 = ["y", [], []] #y=30, y
        data2 = [["a", 10], ["y", 30]]
        result = evalTree(data1, data2)
        self.assertEqual(30, result)

    def testBasicExpression(self):
        data1 = ["+", ["x", [], []], ["y", [], []]] #x=1, y=2; x+y
        data2 = [["x", 1], ["y", 2]]
        result = evalTree(data1, data2)
        self.assertEqual(3, result)

    def testLongExpression(self):
        data1 = ["-", ["+", ["x", [], []], ["y", [], []]], ["/", ["*", ["z", [], []], ["a", [], []]], ["b", [], []]]] #x=30, y=20, z=100, a=10, b=5; x+y-z*a/b
        data2 = [["x", 30], ["y", 20], ["z", 100], ["a",10], ["b",5]]
        result = evalTree(data1, data2)
        self.assertEqual(-150, result)

    def testDivisionByZero(self):
        data1 = ["/", ["x", [], []], ["0", [], []]] #x=1; x/0
        data2 = [["x", 1]]
        result = evalTree(data1, data2)
        self.assertEqual(None, result)

    def testMissingVariable(self):
        data1 = ["+", ["x", [], []], ["y", [], []]] #x=1; x/y
        data2 = [["x", 1]]
        result = evalTree(data1, data2)
        self.assertEqual(None, result)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
from pythonds.basic import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["!"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        elif token == "!":
            operand1 = operandStack.pop()
            result = doMath("!", operand1, None)
            operandStack.push(result)
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "!":
        return factorial(op1)
    else:
        return op1 - op2

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def infixToPostfixEval(infixexpr):
    print(infixToPostfix(infixexpr), "\nEvaluates to: ", postfixEval(infixToPostfix(infixexpr)))
    return [infixToPostfix(infixexpr), postfixEval(infixToPostfix(infixexpr))]
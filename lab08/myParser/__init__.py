def precedence(oper):
    if oper in ['+', '-']:
        return 1
    elif oper in ['*', '/']:
        return 2
    else:
        return 3

#Returns if x is an operator
def operatorp(x):
    return x in ['+', '-', '/', '*', '!']

#Return if x is a number
def numberp(x):
    return not operatorp(x)

#Return if x is parenthesized
def paranthesized(x):
    return type(x) is list

#Parse method
def parse(expr):
    return parseHelper(expr, [], [])

def parseHelper(expr, operators, operands):
    if expr == []:
        if operators == []:
            return operands[0]
        else:
            return handleOp([], operators, operands)
    elif paranthesized(expr[0]):
        return parseHelper(expr[1:], operators, [parseHelper(expr[0], [], [])]+operands)
    elif numberp(expr[0]):
        return parseHelper(expr[1:], operators, [[expr[0], [], []]]+operands) #Set root value to number
    elif operators == [] or precedence(expr[0]) > precedence(operators[0]):
        return parseHelper(expr[1:], [expr[0]]+operators, operands)
    else:
        return handleOp(expr, operators, operands)

def handleOp(expr, operators, operands):
    if operators[0] == '!':
        return parseHelper(expr, operators[1:], [[operators[0], operands[0], []]]+operands[1:])
    return parseHelper(expr, operators[1:], [[operators[0], operands[1], operands[0]]]+operands[2:])

#x=['3','/','6','-', '9']
#x=['4', '+', '3', '*', '7']
#x=[['4'], '+', ['3'], '+', '6']
#x="( 4 + 3 * 7 - 5 / ( 3 + 4 ) + 6 )"
#x=[['4', '+', '3'], '*', '7']
x=['7', '*', ['3', '+', '4'], '!']
print("--", parse(x))

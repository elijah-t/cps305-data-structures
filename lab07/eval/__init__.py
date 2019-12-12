def evalTree(tree, environment):
    root = tree[0]
    left_subtree = tree[1]
    right_subtree = tree[2]
    if left_subtree == [] and right_subtree == []:
        if root.isdigit():
            root = int(root)
            return root
        for i in range(len(environment)):
            if environment[i][0] == root:
                root = environment[i][1]
        return root
    if root in "+-*/":
        leftBranch = evalTree(left_subtree, environment)
        rightBranch = evalTree(right_subtree, environment)
        return doMath(root, leftBranch, rightBranch)

def doMath(op, op1, op2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if str(op1) in alphabet or str(op2) in alphabet:
        return None
    elif op == "*":
        return int(op1) * int(op2)
    elif op == "/":
        if int(op2) == 0:
            return None
        return int(op1) / int(op2)
    elif op == "+":
        return int(op1) + int(op2)
    else:
        return int(op1) - int(op2)



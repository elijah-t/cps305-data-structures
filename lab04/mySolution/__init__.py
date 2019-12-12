import turtle
import random

def tree(branchLen,t):

    if branchLen < 25:
        t.color("green")
    else:
        t.color("brown")
    
    if branchLen > 5:
        t.pensize(branchLen / 5)
        random_angle = random.randint(5, 30)
        random_branch = random.randint(5, 7)
        t.forward(branchLen)
        t.right(random_angle)
        tree(branchLen-random_branch,t)
        t.left(random_angle * 2)
        tree(branchLen-random_branch,t)
        t.right(random_angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    turtle.tracer(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")
    tree(75,t)
    myWin.exitonclick()

#Exercise 2

def power(x, n, acc=1):
    if n == 0:
        return acc
    else:
        acc *= x
    return power(x, n-1, acc)

def powerH(x, n):
    if n == 1:
        return x
    else:
        if n % 2 == 0:
            return powerH(x, n/2) * powerH(x, n/2)
        else:
            return x * powerH(x, n/2) * powerH(x, n/2)

def C(n, k):
    if k == 0 or k == n:
        return 1
    elif n > k > 0:
        return C(n-1, k) + C(n-1, k-1)
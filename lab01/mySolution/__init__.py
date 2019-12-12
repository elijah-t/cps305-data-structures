import random
import matplotlib.pyplot as plt

def generate(lenTarget, lenKey, key):
    return [key[random.randrange(lenKey)] for i in range(lenTarget)]

def calcScore(string, target):
    score = 0
    for i in range(len(string)):
        if string[i] == target[i]:
            score += 1
    return score / len(target) * 100

def monkeyTypist():

    target = list("methinks it is like a weasel")
    lenS = len(target)
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")
    lenA = len(alphabet)
    
    bestScore = 0
    bestStr = generate(lenS, lenA, alphabet)
    newStr = generate(lenS, lenA, alphabet)
    newScore = calcScore(newStr, target)
    index = 0

    scoreList = []
    timesList = []
    timesRun = 0

    print("String                       Score             Iteration")
    while index <= lenS:
        if index == lenS:
            print("%s %.5f %14d" %("".join(bestStr), bestScore, timesRun))
            scoreList.append(bestScore)
            timesList.append(timesRun)
            break
        if newStr[index] != target[index]:
            newStr[index] = alphabet[random.randrange(lenA)]
        else:
            index += 1
        if newScore > bestScore:
            bestScore = newScore
            bestStr = newStr
            scoreList.append(bestScore)
            timesList.append(timesRun)
        if timesRun % 100 == 0:
            print("%s %.5f %15d" %("".join(bestStr), bestScore, timesRun))
        newScore = calcScore(newStr, target)
        timesRun += 1
    plt.scatter(timesList, scoreList, color='r', marker='+')
    plt.xlabel("Iteration")
    plt.ylabel("Score of Best String")
    plt.show()
        
monkeyTypist()

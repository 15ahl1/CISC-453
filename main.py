import random

optimalAction = {}
stateValues = {}
possibleStates = ["?"]

# "States don't need to be represented"


def init():
    for state in possibleStates:
        optimalAction[state] = getRandomAction(state)
        stateValues[state] = random.random() * 100  # rand float 0-100


def policyEval():
    minAccuracy = 0.01
    delta = 0
    alpha = 0.001
    value = None
    while delta < minAccuracy:
        delta = 0
        for state in possibleStates:
            value = stateValues[state]
            stateValues[state] = sum()  # TODO
            delta = max(delta, abs(value - stateValues[state]))


def policyImprove():
    policyStable = True
    oldAction = None
    while policyStable:
        for state in possibleStates:
            oldAction = optimalAction[state]
            optimalAction[state] =  # TODO argmax...
            if oldAction != optimalAction[state]:
                policyStable = False
        if policyStable:
            return
        else:
            policyEval()


def getRandomAction():
    # 'Lie' means help accomplice, 'Confess' means help police
    possibleActions = ["confess", "lie"]
    return random.choice(possibleActions)

# Rewards are from Perspective of P1
# For Prisoner's Dilemma


def getReward(p1, p2):
    if p1 == "lie" and p2 == "lie":
        return 5
    elif p1 == "lie" and p2 == "confess":
        return 0
    elif p1 == "confess" and p2 == "lie":
        return 10
    else:  # confess / confess
        return 1


init()

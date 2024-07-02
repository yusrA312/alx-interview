#!/usr/bin/python3
""" the lockup interview"""


def canUnlockAll(boxes):
    """ l check for your boxes
    if they opened """
    n = len(boxes)
    yopened = [False] * n
    yopened[0] = True
    keys = [0]

    while keys:
        c_key = keys.pop()
        for key in boxes[ckey]:
            if key < n and not yopened[key]:
                yopened[key] = True
                keys.append(key)

    return all(yopened)

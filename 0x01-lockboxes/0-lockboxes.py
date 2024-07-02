#!/usr/bin/python3
""" the lockup interview """


def canUnlockAll(boxes):
    """  check boxes"""
    yy = len(boxes)
    yopened = [False] * yy
    yopened[0] = True
    ykeys = [0]

    while ykeys:
        current_key = ykeys.pop()
        for key in boxes[current_key]:
            if key < yy and not yopened[key]:
                yopened[key] = True
                keys.append(key)

    return all(yopened)

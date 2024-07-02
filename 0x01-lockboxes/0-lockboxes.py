#!/usr/bin/python3
""" This module has the answer to the lockup interview question """


def canUnlockAll(boxes):
      '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    # Number of boxes
    
    num = len(boxes)
    OP = [False] * num
    OP[0] = True
    keys = [0]
    
     # Traverse boxes
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < num and not OP[key]:
                OP[key] = True
                keys.append(key)

    return all(OP)

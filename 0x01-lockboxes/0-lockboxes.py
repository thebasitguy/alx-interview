#!/usr/bin/python3
"""This script unlocks a list of lists."""


def canUnlockAll(boxes):
    """This function takes a list of lists and the content
       of a particular list unlocks other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False

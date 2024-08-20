#!/usr/bin/python3
""" this file contains a script that determine
the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a
    given amount total by given a pile of coins of
    different values
    """

    if total <= 0:
        return 0

    cou = 0
    re = total
    idx = 0
    sorted_list_coins = sorted(coins, reverse=True)
    n = len(coins)
    while re > 0:
        if idx >= n:
            return -1
        if re - sorted_list_coins[idx] >= 0:
            re -= sorted_list_coins[idx]
            cou += 1
        else:
            idx += 1
    return coun

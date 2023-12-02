#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:44:36 2020

@author: waldo
Simulate the rolling of the dice. Print the total.
"""
import random
import sys

def toss_die():
    return (random.randint(1,6))

def toss_dice(num_dice):
    total = 0
    for i in range(0, num_dice):
        total += toss_die()
    return total

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: toss_dice number_of_dice')
        sys.exit(1)
    try:
        num_dice = int(sys.argv[1])
    except:
        print('Usage: toss_dice number_of_dice: Number of dice must be an integer')
        sys.exit(1)

    print('You rolled a total of', toss_dice(num_dice))
    sys.exit(0)
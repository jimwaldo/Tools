#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:44:36 2020

@author: waldo
Simulate the rolling of the dice. Print the value of each die, along with the total.
"""
import random
import sys


def toss_die(facets=6):
    '''Return a random value from 1 to facets (default 6)'''


    return (random.randint(1, facets))


def toss_dice(num_dice, facets=6):
    '''Return a list of random values from 1 to facets (default 6) for num_dice dice,'''
    dice_values = []
    total = 0
    for i in range(0, num_dice):
        value = toss_die(facets)
        dice_values.append(value)
        total += value
    return dice_values, total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: toss_dice number_of_dice [number_of_facets]')
        sys.exit(1)
    try:
        num_dice = int(sys.argv[1])
        facets = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    except:
        print('Usage: toss_dice number_of_dice [number_of_facets]: Arguments must be integers')
        sys.exit(1)

    values, total = toss_dice(num_dice, facets)
    print('You rolled:', values)
    print('Total:', total)
    sys.exit(0)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create a random set of numbers from 1 to range_top. Print the set, in sorted order
"""

import sys, random


def make_rand_set(num, range_top):
    """
    Create a random set of numbers of length num from 1 to range_top.
    :param num: the length of the set of random numbers
    :param range_top: The maximum value of a random number in the set
    :return: A set of lentgh num of random numbers from 1 to range_top
    """
    ret_set = set()
    while len(ret_set) < num:
        ret_set.add(random.randint(1, range_top))

    return ret_set


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python getRandomSet number_in_set range_of_set')
        sys.exit(1)

    try:
        set_size = int(sys.argv[1])
        set_max = int(sys.argv[2])
    except:
        print('Usage: python getRandomSet number_in_set range_of_set, where number_in_set and range_of_set are integers')
        sys.exit(1)

    if set_size > set_max:
        print('invalid input: number in set must be less than range of set')
        sys.exit(1)

    p_list = list(make_rand_set(set_size, set_max))
    p_list.sort()
    print(', '.join(str(x) for x in p_list))


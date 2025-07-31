#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Using a pickle file containing a list of names, create a random set of names. The program
also takes a pickle file of names to be excluded from the random set. The final input is
the number of entries in the random set. The program prints the random set to standard out.
If there are not enough entries that are not in the exclude file to create a set of the
requested size, the program prints an error message and exits. Any names added to the
set are added to a new exclude file.
"""

import os
import pickle
import random
import sys


def print_error():
    print("usage: python getRandomEntries.py name_file exclude_file num_entries")


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print_error()
        sys.exit(1)
    else:
        num_choice = int(sys.argv[3])
        namefile = open(sys.argv[1], 'rb')
        nameList = pickle.load(namefile)
        namefile.close()

    ex_name = sys.argv[2]

    if os.path.exists(ex_name):
        exclude_file = open(ex_name, 'rb')
        exclude_set = pickle.load(exclude_file)
        exclude_file.close()
    else:
        exclude_set = set()

    choice_list = []
    random.shuffle(nameList)

    for n in nameList:
        if n not in exclude_set:
            choice_list.append(n)
            exclude_set.add(n)
        if len(choice_list) >= num_choice:
            break

    if len(choice_list) < num_choice:
        print('Unable to find', num_choice, "names not in the exclude list")

    for n in choice_list:
        print(n)

    exclude_file = open(ex_name, 'wb')
    pickle.dump(exclude_set, exclude_file)
    exclude_file.close()

#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 4 15:00:00 2019
Tool to take in the .csv file from the canvas and create a list of names. Assumes that the first
three lines of the file are header lines. Assumes that the names are a single entry as a string,
of the form "Lastname, Firstname".
"""

import csv
import pickle
import sys


def reverse_name(name):
    """
    Takes in a name in the form "Lastname, Firstname" and returns the name in the form "Firstname Lastname"
    """
    name_l = name.split(', ')
    return " ".join([name_l[1] + ' ' + name_l[0]])


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: makeRosterFromCanvas.py rosterFile.csv outfile.pkl')
        sys.exit(1)

    fin = csv.reader(open(sys.argv[1], 'r'))
    # Start by skipping the header lines
    l = next(fin)
    while ',' not in l[0]:
        l = next(fin)

    name_list = [reverse_name(l[0])]

    for l in fin:
        name_list.append(reverse_name(l[0]))

    # Get rid of the last line of the file, if it is a test student
    if name_list[-1] == 'Test Student':
        name_list = name_list[:-1]

    pickle.dump(name_list, open(sys.argv[2], 'wb'))

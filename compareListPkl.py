#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Compare the entries in two lists, each stored in a pickle file. Print out the
entries of each list that do not occur in the other, or that the contents is the
same in both lists.
"""

import sys
import pickle


def get_list(f_name):
    """
    Get the list from a pickle file.
    :param f_name: the name of the pickle file
    :return: the list stored in the pickle file
    """
    f = open(f_name, 'rb')
    l = pickle.load(f)
    f.close()
    return l


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage compareListPkl.py file1.pkl file2.pkl')
        sys.exit(1)

    set_1 = set(get_list(sys.argv[1]))
    set_2 = set(get_list(sys.argv[2]))

    in_1_not_2 = list(set_1 - set_2)
    in_2_not_1 = list(set_2 - set_1)
    if len(in_1_not_2) > 0:
        print('items in', sys.argv[1], 'not in', sys.argv[2])
        print('; '.join(in_1_not_2))
    else:
        print('All items in', sys.argv[1], 'occur in', sys.argv[2])
    if len(in_2_not_1) > 0:
        print('items in', sys.argv[2], 'not in', sys.argv[1])
        print('; '.join(in_2_not_1))
    else:
        print('All items in', sys.argv[2], 'occur in', sys.argv[1])

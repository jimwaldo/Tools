# -*- coding: utf-8 -*-
"""
Spyder Editor

Pair up groups of people in a random way and assign them to a table. If there 
is a group left over, add it to the last group. Write the reesults to a text file.
Input is a file that contains a pickle of a list of lists, where the individual
lists are identifiers for the group.
"""

import pickle, random, sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python pairGroups.py group_file.pkl out_file.txt')
        sys.exit(1)
        
    fin = open(sys.argv[1], 'rb')
    group_l = pickle.load(fin)
    fin.close()
    
    random.shuffle(group_l)
    
    if (len(group_l)) % 2 == 0:
        group_max = len(group_l)
    else:
        group_max = len(group_l) -1
        
    group_pairs = []
    for i in range(0, group_max, 2):
        group_pairs.append([group_l[i], group_l[i+1]])
    if group_max < len(group_l):
        group_pairs[-1].append(group_l[-1])
        
        
    table_num = 1
    out_f = open(sys.argv[2], 'w')
    for i in range(0, group_max, 2):
        out_f.write("Table " + str(table_num) + ": ")
        out_f.write("")
        
    

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
    if len(sys.argv) < 4:
        print('Usage: python makeTableAssignments.py group_file.pkl out_file.txt num_per_table')
        sys.exit(1)
        
    fin = open(sys.argv[1], 'rb')
    group_l = pickle.load(fin)
    fin.close()
    
    random.shuffle(group_l)

    num_per_table = int(sys.argv[3])
    remainder = len(group_l) % num_per_table
    if remainder == 0:
        group_max = len(group_l)
    else:
        group_max = len(group_l) - 1
        
    group_pairs = []
    for i in range(0, group_max, num_per_table):
        group = []
        for j in range(0, num_per_table, 1):
            group.append(group_l[i+j])
        group_pairs.append(group)

    if remainder != 0:
        group = [];
        for i in range(0, remainder,1):
            group.append(group_l[:i])
        group_pairs.append(group)
        
        
    table_num = 1
    out_f = open(sys.argv[2], 'w')
    for g in group_pairs:
        out_f.write("Table " + str(table_num) + ": ")
        out_f.write(", ".join(g))
        out_f.write('\n')
        table_num += 1
        
    out_f.close()
    
    

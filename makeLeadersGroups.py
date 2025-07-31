#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create a list of groups of students, including a designated leader of the group. The
group will be created by selecting from the list included in the list contained
in the pickle file read in as the first argument. The leaders will be picked form that
list as well, but will exclude those named in the list contained in the pickle file
named by the second argument. The number of groups will be determined by the integer
provided as the third argument. Those picked as leaders will be added to the exclude
as leaders list, which will overwrite the pickle file in the second argument.

The groups will be printed to standard output, with the name of the leader first in
the list.
"""

import pickle
import random
import sys
import os.path


def read_pickle(filename):
    """
    Read a pickle file and return the contents
    """
    fhandle = open(filename, 'rb')
    data = pickle.load(fhandle)
    fhandle.close()
    return data


def write_pickle(filename, data):
    """
    Write a pickle file with the supplied name and data
    """
    fhandle = open(filename, 'wb')
    pickle.dump(data, fhandle)
    fhandle.close()


def chose_leaders(candidates, num_leaders):
    """
    Choose a random number of leaders from the list of candidates.
    """
    leaders = []
    random.shuffle(candidates)
    for i in range(0, num_leaders):
        leaders.append([candidates[i]])
    return leaders


def extend_leader_group(cur_list, lead_list):
    """
    Extend the list of leaders by adding the leaders from the list of leaders. The leader is the first
    entry in each of the lists that make up the current (group) list.
    """
    cur_leads = set()
    for l in cur_list:
        lead_list.append(l[0])
        cur_leads.add(l[0])

    return cur_leads


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage makeGradingGroups classFileName excludeFileName numberOfGroups')
        sys.exit(0)
    classFName = sys.argv[1]
    leaderFName = sys.argv[2]
    if os.path.exists(leaderFName):
        leaderList = read_pickle(leaderFName)
    else:
        leaderList = []
    try:
        numGroups = int(sys.argv[3])
    except:
        print('Number of groups must be an integer')
        sys.exit(1)

    classList = read_pickle(classFName)

    class_s = set(classList)
    leader_s = set(leaderList)
    cand_leaders = list(class_s - leader_s)
    if len(cand_leaders) < numGroups:
        print('Not enough candidates for leaders')
        sys.exit(1)
    group_list = chose_leaders(cand_leaders, numGroups)
    cur_leads = extend_leader_group(group_list, leaderList)
    write_pickle(leaderFName, leaderList)
    remain_l = list(class_s - cur_leads)
    random.shuffle(remain_l)
    i = 0
    for c in remain_l:
        group_list[i].append(c)
        i = (i + 1) % numGroups

    for g in group_list:
        print(', '.join(c for c in g))
        print('\n')

    sys.exit(0)

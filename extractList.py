#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:58:08 2023

@author: waldo
"""
extract_list = [0,1,2,3,4,5,`4,15,16,17,18,19]

def build_extract_list(from_iter, index_list):
    extract = []
    for l in from_iter:
        e = []
        for i in index_list:
            e.append(l[i])
        extract.append(e)
    return extract

def get_distribution(from_l,i):
    g_total = 0
    bins = [0,0,0,0,0]
    for l in from_l:
        if l[i] == '':
            tot = 0.0
        else:
            tot = float(l[i])
        g_total += tot
        if tot < 1.0:
            bins[0] += 1
        elif tot < 10.0:
            bins[1] += 1
        elif tot < 100.0:
            bins[2] += 1
        elif tot < 1000.0:
            bins[3] += 1
        else:
            bins[4] += 1
            
    return g_total, bins

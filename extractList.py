#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:58:08 2023

@author: waldo
"""

def build_extract_list(from_iter, index_list):
    extract = []
    for l in from_iter:
        e = []
        for i in index_list:
            e.append(l[i])
        extract.append(e)
    return extract
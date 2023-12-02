#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:23:38 2020

@author: waldo
"""
import random

def flip_coin():
    toss = random.randint(0, 1)
    if toss == 0:
        return "heads"
    else:
        return "tails"
    
if __name__ == '__main__':
    print (flip_coin())
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:23:31 2020

@author: waldo
"""
import random

coin = ["heads", "tails"]
def flip_coin2():
    random.shuffle(coin)
    return coin[0]

if __name__ == '__main__':
    print(flip_coin2())
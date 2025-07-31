#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:30:19 2024

@author: waldo
"""
def sort_by_last_name(names):
    # Define a custom sorting key that extracts the last name
    def get_last_name(name):
        return name.split()[-1]

    # Sort the names using the custom sorting key
    sorted_names = sorted(names, key=get_last_name)
    return sorted_names

# Example list of names
names = [
    "John Smith",
    "Alice Johnson",
    "Bob White",
    "David Brown",
    "Emily Adams"
]

# Sort the names by last name
sorted_names = sort_by_last_name(names)

# Print the sorted names
for name in sorted_names:
    print(name)

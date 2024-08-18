# ======================
# PROGRAM : Company Logo
# ======================

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

# Variables 01
data = dict()
result = []


def getKey(dic, value):
    '''get the key from dic'''
    for key in dic:
        if dic[key]==value:
            return key
    return None


if __name__ == '__main__':
    name = input() # Input
    
    # Variables 02
    allChars = list(name)
    chars = list(set(allChars))
    chars.sort()
    
    # set the data(sorted)
    for char in chars:
        data[char] = allChars.count(char)

    # make the values
    values = list(data.values()) # get the all values
    values.sort()
    values.reverse()

    # make the result
    for val in values:
        crntKey = getKey(data, val)
        result.append([str(crntKey), str(val)]) # make the result
        del data[crntKey]

    # Output
    for i in range(3):
        print(' '.join(result[i]))
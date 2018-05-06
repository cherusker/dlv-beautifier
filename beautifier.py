#!/bin/python3

import re
import sys

if __name__ == "__main__":
    lines = sys.stdin.read().strip(' \t\r\n').split('\n')
    as_count = 0
    for line in lines:
        if line == '':
            continue
        as_count += 1
        print("Answer set " + str(as_count) + ":")
        items = line.strip(' \t\r\n{}').split(', ')
        items.sort()
        for item in items:
            if not item.startswith('-'):
                print('  ' + item.replace('(', ' ( ').replace(')', ' )').replace(',', ', '))
    if as_count < 1:
        print("No answer set")

#!/bin/python3

import sys

if __name__ == "__main__":
    lines = sys.stdin.read().split('\n')
    for line in lines:
        if line == '':
            continue
        print("Answer set:")
        items = line.replace('{', '').replace('}', '').replace('\n', '').split(', ')
        items.sort()
        for item in items:
            if not item.startswith('-'):
                print('  ' + item.replace('(', ' ( ').replace(')', ' )').replace(',', ', '))

#!/usr/bin/env python3

# Sara Clarin
# Challenge06: find longest sequence of consecutive, distinct items in a list


import sys

fruitDict = {}    # use dictionary as a set to preserve order

def find_distinct_fruits( line):
    sequence = []
    max_sequence = []
    max_len = 0
    left = 0
    right = 1
    fruitDict[line[left]] = 0

    while right < len(line):    # use two iterators for moving window

       if line[right] in fruitDict:         # we have seen this fruit before
            sequence = line[left:right]

            if len(sequence) > max_len:
                max_sequence = sequence
                max_len = len(sequence)

            fruitDict.clear()
            left += 1
            right = left
       
       fruitDict[line[right]] = 0       # add right index to dict
       right += 1
                
    if len(fruitDict) > 0 and len(fruitDict) > max_len:   # no duplicates case
        max_sequence = list(fruitDict.keys())
        
    fruitDict.clear()
    return max_sequence


def main():

    for  line in sys.stdin.readlines():
       max_sequence = find_distinct_fruits( line.strip().split())
       l = len(max_sequence)
       print(f"{l}: {', '.join(max_sequence)}")


if __name__ == "__main__":
    main()

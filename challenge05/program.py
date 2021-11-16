#!/usr/bin/env python3

# Sara Clarin
# Challenge05: program to determine the max and the argmax cycle length

import sys
import collections


collatz_dict = {}

def find_max_cycle(a , b):

    max_cycle = 0
    max_length = 0
    #count = 0

    for i in range(a, b): 
        n = i
        count = 1
        #if n  == 1:         # done w/n value, continue to next iteration
            #continue
        while (n > 1):
            count += 1
            #print(n)
        # calculate collatz, 1.) store all numbers printed as a list, take key=n, val = list and then have another list val=len(list)
            if n % 2 == 1:
                n = 3*n + 1
            else: 
                n = n/2
        collatz_dict[i] = count

    # option 2: calculate collatz, use naive max function to 
    max_key = max(collatz_dict, key=collatz_dict.get)
    max_value = max(collatz_dict.values())

    #print(f'key: {max_key} value: {max_value}')
    print(f'{a} {b} {max_key} {max_value}')
    collatz_dict.clear()


def main():
    for line in sys.stdin.readlines():
        i, j = map(int, line.strip().split())
        #print(i, j)
        find_max_cycle(i, j)


if __name__ == "__main__":
    main() 

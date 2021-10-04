#!/usr/bin/env python3

# Author: Sara Clarin
# Sussy Dogecoin Transactions: program to calculate the minimum number of steps required to reach input target, when previous value can only be doubled or +1
#
# 4 October 2022

import sys


# Functions

def get_dogecoins( n,  table={} ):

    # initialize table, insert base cases
    table = [0] * (n+1)

    table[0] = 0
    table[1] = 1
 
    # Build bottom-up table of optimal solutions
    for i in range(2, n + 1):

        if not table[i]:

            if i % 2 :                   # n is odd
                table[i] = table[i-1] + 1
            else:                        # n is even
                table[i] = min(table[i//2], table[i-1]) + 1

    return table[n]

# Main Execution
def main():

    cache = {}
    for index,target in enumerate(map(int, sys.stdin), 1):
        min_tx = get_dogecoins( target,  cache)
        print(f'{index}. Minimum number of doge transactions: {min_tx}')



if __name__ == "__main__":
    main()

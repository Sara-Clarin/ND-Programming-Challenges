#!/usr/bin/env python3


import sys

# create cache


# functions

def get_dogecoins( n, tx, table={} ):

    # initialize table, insert base cases
    table = [0] * (n+1)

    table[0] = 0
    table[1] = 1

    #base case: except no recursion??
    #if n == 1:
        #return table[1]

    tx = 0
  
    # Build bottom-up table of optimal solutions
    for i in range(2, n + 1):
        if not table[i]:

            if i % 2 :     # n is odd
                table[i] = table[i-1] + 1
            else:           # n is even
                table[i] = min(table[i//2], table[i-1]) + 1
    #print(coinsum)

    print("Table:")
    count = 0
    for item in table:
        print(f't[{count}]: {item}')
        count += 1

    return table[n]


# main execution

def main():

    cache = {}

    for index,target in enumerate(map(int, sys.stdin), 1):
        print(f'input: {target}')

        min_tx = get_dogecoins( target, 0 , cache)
        print(f'{index}. Minimum number of doge transactions: {min_tx}')

if __name__ == "__main__":
    main()

#!/usr/bin/env python3


import sys

MOVES = {
    '1': '68',
    '2': '79',
    '3': '48',
    '4': '039',  
    '5': ' ',
    '6': '017',
    '7': '26',
    '8': '13',
    '9': '24',
    '0': '46',
    ' ' : ''
}


def find_rook_moves( N, start , sequence):
    '''
    N: the number of steps to continue recursing
    start: the current number
    sequence: the sequence we're building
    '''
    
    # base case: when N = 0 or we've done N steps
    if N == 0:
        return [sequence]
        
    # recursive step
    results = []
    for move in MOVES[start]:
         results.extend(
             find_rook_moves( N-1,  move  , sequence + start )
         )
    
    results = remove_duplicates(results)
    return results

def remove_duplicates( results):

    for ind, value in enumerate(results):
        if ind >= 1 and value == results[ind -1]:
            del results[ ind -1]
            
    return results


def main():
    count = 0
    for line in sys.stdin:
        start, hops = line.strip().split()

        if count > 0:
            print("")

        for path in find_rook_moves( int( hops)  , start, ""):
            print(path)

        count += 1

if __name__ == "__main__":
    main()

#!/usr/bin/env python3


import sys

MOVES = {
    '1': '68',
    '2': '79',
    '3': '49',
    '4': '039',   # omit 5 because it's never solution
    '6': '017',
    '7': '26',
    '8': '13',
    '9': '24',
    '0': '46'
}

def find_rook_moves( N, start , sequence):
    '''
    N: the number of steps to continue recursing
    start: the current number
    sequence: the sequence we're building
    '''
    

    # base case: when N = 0 or we've done N steps
    if ( N == 0):
        return [sequence]
        #print(sequence)
        
    # recursive step
    results = []
    for move in MOVES[start]:
        #print(move)
        #sequce = sequence +  (find_rook_
        results.extend(

            find_rook_moves( N-1,  move  , sequence + start )
        )

    return results


def main():
    for line in sys.stdin:
        start, hops = line.strip().split()
        print(f'{start} {hops}')
        sequence = find_rook_moves( int( hops) , start, "")
        print(sequence)

if __name__ == "__main__":
    main()

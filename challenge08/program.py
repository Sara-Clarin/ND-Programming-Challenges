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

#results = []

def find_rook_moves( N, start , sequence, totalmoves):
    '''
    N: the number of steps to continue recursing
    start: the current number
    sequence: the sequence we're building
    '''
    
    # base case: when N = 0 or we've done N steps
    #if ( N <= 0):
    if len(sequence) == totalmoves:
        return [sequence]
        #print(sequence)
        #return
        
    # recursive step
    results = []
    #results.extend( sequence)
    count = 1
    for ind, move in enumerate(MOVES[start]):
        #print(move)
        #sequce = sequence +  (find_rook_
         #if count == 2:

         
         #dummy = find_rook_moves( N-1,  move  , sequence + start, totalmoves )
         #if ind > 1 and results[ind - 1 ] != dummy:
         results.extend(
             find_rook_moves( N-1,  move  , sequence + start, totalmoves )
         )
         #count += 1    
    
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

        for path in find_rook_moves( int( hops)  , start, "", int(hops)):
            print(path)

        count += 1

if __name__ == "__main__":
    main()

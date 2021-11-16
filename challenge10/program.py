#!/usr/bin/env python3


import sys

LEGOS = [ "4", "3", "2", "1" ]

def brick_rows_greedy( legolist ):
    ''' 
    legolist: sorted list of bricks
    rows: the minimum number of rows required to store
    strategy: place the largest legos first
    '''
    rows = 0

    while legolist:

        lego = legolist.pop(0)
        remainder = 4 - lego

        i = 0
        while remainder > 0 and i < len(legolist):
 
            if legolist[i] <= remainder:
                lego2 = legolist.pop(i)
                remainder -= lego2
            else:
               i  += 1

        rows += 1

    return rows


def build_legolist( numlist ):
    '''
    Given an input in the form { #1's, #2's, #3's #4's } 
    output a list in the form { 4, 4, 4, 3, 2, 1, 1 }
    an 
    '''
    legolist = []

    numlist.reverse()
    index = 0
    for legocount in numlist:
        for i in range(legocount):
            legolist.append( int(LEGOS[index] ) )

        index += 1

    return legolist


def main():

    for line in sys.stdin.readlines():
        line = list( map(int, line.strip().split()))
        legolist = build_legolist( line)
        rows =  brick_rows_greedy( legolist)
        print(rows)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3


import sys

LEGOS = [ "4", "3", "2", "1" ]


def brick_rows_greedy( legolist ):
    ''' 
    legolist: sorted list of bricks
    rows: the minimum number of rows required to store
    '''
    rows = 0

    


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
        #print(index)
        for i in range(legocount):
           # print(i)
            legolist.append( LEGOS[index] )

        index += 1

    #print(legolist)


def main():


    for line in sys.stdin.readlines():
        line = list( map(int, line.strip().split()))
        
        print(line)
        legolist = build_legolist( line) 
        rows = brick_rows_greedy( legolist )


if __name__ == "__main__":
    main()

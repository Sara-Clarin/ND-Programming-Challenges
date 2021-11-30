#!/usr/bin/env python3

import sys, math

# Least Perfect Squares
# Author: Sara Clarin
# 29 November 2021

def get_min_square( num):
    '''
    Num: limit of the DP table, input integer
    Bottom-Up DP solution finding optimal square combination less than index
    '''
    if num <=3:
        return num
    if math.sqrt( num) % 1 == 0:
        return 1
    if num == 8:
        return 2

    table = [ sys.maxsize for i in range(num+ 1)]  # start at 0

    # Base Cases: all indexes that are squares have count = 1
    table[0] = 0
    table[1] = 1
    table[2] = 2
    table[3] = 3
    
    for i in range( int( math.floor( math.sqrt( num )))): 
        square = i*i
        table[square] = 1

    # Build Table
    for i in range(2, num +1):
        j = 1
        while True:   # go through squares smaller than current index
            if i - (j*j) < 0:
                break
            else:
                table[i] = min( table[i], table[i - (j*j)] + 1)
            j += 1

    return table[num]

def main():

    for integer in map(int, sys.stdin):
        minimum = get_min_square( integer)
        print(minimum)


if __name__ == "__main__":
    main()
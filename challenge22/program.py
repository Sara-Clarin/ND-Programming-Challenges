#!/usr/bin/env python3

import sys, math


def build_squares_table():
    sq_table = [ 0 for i in range(100) ]
    print(sq_table)
    for i in range(100):
        sq_table[i] = i*i
    
    return sq_table

def find_least_squares( squares, num ):
    remainder = num
    squarecount = 0
    i = math.floor( math.sqrt( num) )

    while i > 0:
        Try = num - squares[ i]
        if Try > 0:
            remainder = Try
            num -= squares[i]
            squarecount += 1
            print(f'{num} - {squares[i]} = remainder: {remainder}')
        else:
            i -= 1

    return squarecount

def get_min_square( num):
    print( f'number is {num}')
    if num <=3:
        return num
    if math.sqrt( num) % 1 == 0:
        return 1
    if num == 8:
        return 2

    table = [ sys.maxsize for i in range(num+ 1)]  # start at 0

    # base cases: all indexes that are squares have count = 1
    table[0] = 0
    table[1] = 1
    table[2] = 2
    table[3] = 3
    table[4] = 4
    for i in range( int( math.floor( math.sqrt( num )) ) ):
        square = i*i
        table[square] = 1

    for i in range(2, num +1):
        #or j in range( 1, ):
        j = 1
        while True:   # go through squares smaller than current
            if i - (j*j) < 0:
                break
            else:
                table[i] = min( table[i], table[i - (j*j)] + 1)
            j += 1

    #print( f'table : {table}')
    return table[num]

def main():

    #table = build_squares_table()
    #print(table)

    for integer in map(int, sys.stdin):
        #minimum = find_least_squares( table, integer)
        minimum = get_min_square( integer)
        #print(f'Minsquares in {integer} is {minimum}')
        print(minimum)



if __name__ == "__main__":
    main()
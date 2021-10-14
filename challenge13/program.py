#!/usr/bin/env python3



import sys

def taeho_tree( level, root, array):
    '''Goal: build a string for the number of 
    '''


    print( root ) 
    print( array )
    if level == max_level:
        return 0 
    
    return taeho_tree( level + 1, root, array)

    return 4



def number_of_nodes(  lev: int ):
    

    if lev == 5:
        return 999999

   

    for i in range( 2**lev ):
        print(lev)

    return number_of_nodes( lev + 1)

def split_array( array):
    
    level = 2
    windowsize = len(array) // level
    start =  0
    end = windowsize
    print( array[ start : end])
    
    mid = start + len(array) // 2
    median = array [ mid ]
    print( median)
    del array[ mid ]

    start = end
    end += windowsize
    print( array[ start : end ])
    


def main():

    n = 0
    for line in sys.stdin.readlines():
        array = list( map( int, line.strip().split() ) )
        n = len(array) // 2 

        
    u = 0
    dummy = number_of_nodes( u  )
    split_array( array )

    '''
        if n > 2:
            taeho_tree( 0, array[n], array) 
        else:
            print(array)
    '''


if __name__ == "__main__":
    main()

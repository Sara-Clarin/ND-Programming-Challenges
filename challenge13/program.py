#!/usr/bin/env python3

import sys, math, collections


def MyTree( level, array, nodedict ):
    '''
    array: a sorted array
    level: which level of the "tree" meaning index in dict
    nodedict: { level } : {list of nodes}
    '''
    n = len(array)

    # base cases
    if n  == 0:
        return

    if n  == 1:
        nodedict[ level ].append( array[0] )
        return

    # recursive case: take the median, recurse on either side
    mid = n //  2
    nodedict[level].append( array[mid])    

    MyTree( level + 1, array[0:mid], nodedict)
    MyTree( level + 1, array[mid+1:n], nodedict) 

    return nodedict


def PrintNodeDict( nodedict ):

    for key, value in nodedict.items():
        print( " ".join(str(e) for e in value ) )


def main():

    leveldict = collections.defaultdict( list)

    for line in sys.stdin.readlines():
        nodedict = collections.defaultdict( list )
        array = list( map( int, line.strip().split() ) )

        leveldict = MyTree( 0, array, nodedict) 
        if leveldict:
            PrintNodeDict(leveldict)
            leveldict.clear()  
        else:
            print(" ".join(str(e) for e in array ))      
         

if __name__ == "__main__":
    main()

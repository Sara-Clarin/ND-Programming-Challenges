#!/usr/bin/env python3

import sys, math, collections

def taeho_tree( level, n , array, maxlevel, leaves):
    '''Goal: build a string of the nodes at each level
    '''
    if level == maxlevel:
        #print( "last level ")
        print( " ".join( str(e) for e in leaves ))
        return 

    if level == 0:
        print( array[ n// 2 ])
        leaves.remove( array[ n// 2])
        #del array[ n//2 ]

    else:
        windowsize = n // (2**level)
        start = 0
        end = windowsize - 1
  
        #print( f'*****level {level} ')
        levelstr = ""
        for i in range (2**level):
            #mid = (start + end) // 2
            #mid = 1 + (end - 1) // 2
            mid = math.ceil ( (start + end) / 2)
            print(f'windowsize: {windowsize}')
            print( f"start: {start} end: {end} mid: {mid}")
            median = array [mid ] 
            #leaves.remove( median )

            levelstr = levelstr + " " + str(median)
            #print( median )
            #del array[mid ]
                
            start = end + 1
            end += windowsize
            #end += windowsize - (i + 1)
            #print( array )
    
        print(levelstr.lstrip())
    return taeho_tree( level + 1, n , array, maxlevel, leaves)

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
    
    mid = (start + len(array)) // 2
    median = array [ mid ]
    print( median)
    del array[ mid ]

    start = end
    end += windowsize
    print( array[ start : end ])
    mid = (start + end) // 2
    print( f'Middle: {mid} start: {start} end: {end} windowsize: {windowsize}')
    

# flow pattern: get median
# get left child
# get right child
# recurse on left subset, return
# recurse on right subset

# core issue: if we "recurse left" as our first call, we'll go all the way down that subtree before returning to the right at all. Need some sort of backtracking

#idea: get median. function(

# another idea: have a variable keeping track of what level of recursion we're on. Then we add it to the appropriate list, dict: { level : [ nodes on a level ] }

def MyTree( level, array, nodedict, maxlevel ):
    n = len(array)

    # base cases
    if n  == 0:
        return

    if n  == 1:
        nodedict[ level ].append( array[0] )
        return

    # recursive case
    mid = n //  2
    nodedict[level].append( array[mid])    

    MyTree( level + 1, array[0:mid], nodedict, maxlevel)
    MyTree( level + 1, array[mid+1:n], nodedict, maxlevel) 

    return nodedict

def PrintNodeDict( nodedict ):

    for key, value in nodedict.items():
        print( " ".join(str(e) for e in value ) )

def main():

    n = 0
    leveldict = collections.defaultdict( list)

    for line in sys.stdin.readlines():
        nodedict = collections.defaultdict( list )
        array = list( map( int, line.strip().split() ) )
        arrayset = set(array)
        n = len(array)
        treeheight = math.ceil(math.log2( n )) 
        #print(f' starting array: {array}')
        #taeho_tree( 0, n, array,  treeheight, arrayset  )

        leveldict = MyTree( 0, array, nodedict, treeheight) 
        if leveldict:
            PrintNodeDict(leveldict)
            leveldict.clear()  
        else:
            print("0")      
         
    #u = 0
    #dummy = number_of_nodes( u  )
    #split_array( array )

    '''
        if n > 2:
            taeho_tree( 0, array[n], array) 
        else:
            print(array)
    '''


if __name__ == "__main__":
    main()

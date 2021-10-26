#!/usr/bin/env python3



import sys, math

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
        windowsize = n // (level + 1)
        start = 0
        end = windowsize
        string = ""
  
        #print( f'*****level {level} ')
        levelstr = ""
        for i in range (2**level):
            mid = (start + end) // 2
            #mid = 1 + (end - 1) // 2
            #print(f'windowsize: {windowsize}')
            #print( f"start: {start} end: {end} mid: {mid}")
            median = array [mid ] 
            leaves.remove( median )

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
    


def main():

    n = 0
    for line in sys.stdin.readlines():
        array = list( map( int, line.strip().split() ) )
        arrayset = set(array)
        n = len(array)
        treeheight = math.floor(math.log2( n )) 
        #print(f' starting array: {array}')
        #taeho_tree( 0, n, array,  treeheight, arrayset  )
        
         

        
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

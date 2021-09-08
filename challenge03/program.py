#!/usr/bin/env python3

# Sam's Search: code to find a target within a circular array with unknown pivot
# By Sara Clarin 9/7/2021

import sys



def find_max_index( data ):
    ''' function that finds the maximum of the list in O(logn) time with modified binary search'''
 
    start = 0
    end = len(data)
    n = end 
   
    # only one element in list
    if ( end == 1):
        return 0
 
    while start < end:
        middle = (start + end) // 2
        midpoint = data[middle]
        
        
        if (middle == 0 and middle > data[middle+1]):  #special case of first or last
            return middle

        if midpoint > data[middle-1] and midpoint > data[middle+1]:   # we've found max element
            return middle

        if midpoint > start: # go right
            start = middle + 1

        else:                  # go left
            end = middle - 1
            

    #print(data) 
    return -1


def find_target_binary( numlist , start, end, target):
    ''' Uses the maximum and minimum as start and end values for normal binary search'''
    
    if (start == end):
        return start

    while start < end:
        middle = (start + end) // 2  
        #print(f"middle_index: {middle}")
        midpoint = numlist[middle]
        
        if midpoint == target:
            return middle
    
        if midpoint < target:   #go left
            end = middle -1

        else:                   # go right
            start = middle + 1
          
    return -1
 

def main():
    
    for count,line in enumerate(sys.stdin.readlines()):
        line = line.strip().split()
        #line = [ int(i) for i in line ]
        #n = len(numlist)

        if count % 2 == 0:
            numlist = [ int(i) for i in line ]
            pivot  = find_max_index( numlist ) + 1
            n = len(numlist)
            #print(numlist)
            #print(f'pivot: {pivot}')

        else:
            target = "".join(line)
            target = int(target)
            #target = int(x) for x in line
            #print(f'target: {target}')
            #print(numlist)
            #print(f'Sublist1: {numlist[0:(pivot)]}')
            #print(f'Sublist 2: {numlist[pivot:]}')

            # case not rotated and Bui tricked me
            if numlist[0] < numlist[n-1]:
                index = find_target_binary( numlist, 0, n -1, target)
                if index != -1:
                    print(f'{target} found at index {index}')
            elif numlist[pivot] == target:
                print(f'{target} found at index {pivot}')
            else:
                index1 = find_target_binary( numlist, 0, pivot-1 , target)
                index2 = find_target_binary( numlist, (pivot) , n - 1, target)

                if (index1 != -1 or index2 != -1):
                    print(f"{target} found at index {index1}") if index1 != -1 else print(f"{target} found at index {index2}")
                else:
                    print(f"{target} was not found")


if __name__ == "__main__":
    main()

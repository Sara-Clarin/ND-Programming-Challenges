#!/usr/bin/env python3

# Sam's Search: code to find a target within a circular array with unknown pivot
# By Sara Clarin 9/7/2021

import sys


def find_max_recursive( data, start, end):
    ''' Code to locate the maximum value (and hence the PIVOT) using binary search
    Runs in O(logn) time complexty'''    

    if end < start or not data:
        return -1
    if end == start:
        return start

    middle = (start + end) // 2
    midpoint = data[middle]

    if middle > start and midpoint < data[middle - 1]:
        return (middle - 1)
    if middle < end and midpoint > data[middle + 1]:
        return middle

    if data[start] >= middle:
        return find_max_recursive(data, start, middle -1)
    return find_max_recursive(data, middle + 1, end)

def find_max_binary( numlist):
    ''' function for maximum in the case that the array is NOT ROTATED'''
    index = 0
    previous = numlist[0]
    if len(numlist) == 1:
        return 0
    for number in numlist:
        if previous > number:
            return index
        index += 1
    return 0  
            

def find_target_binary( numlist , target):
    ''' adjusted binary search using pivot as start and end values conditionally'''
    if not numlist:
        return -1

    start = 0
    end = len(numlist) - 1
    pivot = find_max_binary( numlist)

    if target <= numlist[end] and target >= numlist[pivot]: # make subarray decision based on pivot
        start = pivot
    else:
        end = pivot

    while start <= end:
        middle = (start + end) // 2  
        midpoint = numlist[middle]
        
        if midpoint == target:
            return middle
    
        if midpoint < target:   #go right
            start = middle +1

        else:                   # go left
            end = middle - 1
          
    return -1
 

def main():
    
    for count,line in enumerate(sys.stdin.readlines()):
        line = line.strip().split()
        index1 = -1
        index2 = -1
        target = -1


        if count % 2 == 0:                      # every other line is an array
            numlist = [ int(i) for i in line ]
            n = len(numlist)
            if numlist[0] > numlist[n-1]:
                pivot  = find_max_recursive( numlist, 0, n) + 1

        else:
            target = "".join(line)
            target = int(target)
            index = find_target_binary( numlist, target)
            print(f'{target} found at index {index}') if index != -1 else print(f'{target} was not found')

            '''
            if len(numlist) <= 1:
                print(f'{target} found at index 0') if numlist[0] == target else print(f'{target} was not found') 

  
            elif numlist[0] < numlist[n-1]:
                index1 = find_target_binary( numlist, 0, n -1, target)
                print(f'{target} found at index {index1}') if index1 != -1 else print(f"{target} was not found")
            
            #elif len(numlist) == 1 and numlist[0] == target:    
                #print(f'{target} found at index 0')

            elif numlist[pivot] == target:
                print(f'{target} found at index {pivot}')

            else:
                index1 = find_target_binary( numlist, 0, pivot , target)
                index2 = find_target_binary( numlist, pivot , n - 1, target)

                if index1 != -1 or index2 != -1:
                    print(f"{target} found at index {index1}") if index1 != -1 else print(f"{target} found at index {index2}")
                else:
                    print(f"{target} was not found")
                '''

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import sys

def process_input(line):
    return [ map(int, line.split()) ]

def count_masked( mask, bitstream):
    right = 1
    left = 0    
    print("in function")
    count = 0

    for i in range(5):
        test_mask = mask << i
        print(f'{test_mask:08b}')

        if bitstream & test_mask:
            count += 1
   # while right < 9:
        
    return count

def main():

    for mask, bitstream in [ map(int, sys.stdin.readline().split()) ]: 
        #mask, bitstream = process_input(line)
        print(mask)
        print(f'{mask:08b}')
        print(f'{bitstream} : {bitstream:32b}')
        
        count = count_masked( mask, bitstream)
        #mask_string = char
        print(f'Count: {count}')

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import sys, math

HEXVAL = {
    "0": "0",
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    '9' : '9' ,
    "A" : "10",
    "B" : "11",
    "C" : "12",
    "D" : "13",
    "E" : "14",
    "F" : "15"
}


def count_masked2( mask, bitstream, frames):
    count = 0
    target = 15

    
    for i in range( 29 ):     # 32b integer - 3 = #window frames

        test_mask = mask << i
        test_target = target << i

        if (bitstream & test_target) == test_mask:
            count += 1

    return count


def main():

    for index, line in enumerate(sys.stdin.readlines(), 1):
        mask1, bitstream = line.strip().split()
        mask = int(HEXVAL[mask1])
        bitstreamb = int(bitstream)

    
        if bitstreamb > 0:
            stream_bits = math.floor(math.log2(bitstreamb)) + 1
        else:
            stream_bits = 0

        if mask > 0:
            mask_bits = math.floor(math.log2(mask)) + 1   # if mask = 1, bits = 1
        else:
            mask_bits = 0
        
        frames = stream_bits
        count = count_masked2( mask, bitstreamb, frames)

        print(f'{index}. {bitstreamb} contains 0x{mask1} {count} times')

if __name__ == "__main__":
    main()

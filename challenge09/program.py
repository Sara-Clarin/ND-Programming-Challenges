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

def process_input(line):
    return [ map(int, line.split()) ]


def hex_to_binary( val):
    new =  '0'*(4-len(val))+val
    print(val)
    print(f'{new}')
    return new


def count_masked( mask, bitstream, bits):
    right = 1
    left = 0    
    print("in function")
    count = 0

    if bits <= 3:
        frames = 0  # finish if necessary

    else:
        for i in range( bits - 3):
            test_mask = mask << i
            print(f'{test_mask:08b}')

            if bitstream & test_mask:
                count += 1
    return count

def count_masked2( mask, bitstream, frames, num_bitstream):
    right = 1
    left = 0    
    #print("in function")
    count = 0
    target = 15

    if mask > 1:
        for i in range( frames):
            test_mask = mask << i
            test_target = target << i
            #print(f'mask: {test_mask:08b}')
            #print(f'bitstream: {bitstream:08b}')
            #print(f'target: {test_target:08b}')

            if (bitstream & test_target) == test_mask :
                 count += 1
            #print(f'{test_mask:08b} ')
    elif mask == 1:
        for i in range( num_bitstream):
            test_mask = mask << i
            test_target = target << i

            if (bitstream & test_target) == test_mask:
                count += 1

    else:
        for i in range( frames):
            test_mask = mask << i
            test_target = target << i

            if (bitstream & test_target) == 0:
                count += 1

    return count


def main():

    for index, line in enumerate(sys.stdin.readlines(), 1):
        mask1, bitstream = line.strip().split()
        mask = int(HEXVAL[mask1])
        bitstreamb = int(bitstream)

        #print(mask)
        #print(f'{mask:08b}')
        #print(f'{bitstreamb} : {bitstreamb:32b}')
    
        if bitstreamb > 0:
            stream_bits = math.floor(math.log2(bitstreamb)) + 1
        else:
            stream_bits = 0
        #print(f'Bits: {bits}')       

        if mask > 0:
            mask_bits = math.floor(math.log2(mask)) + 1   # if mask = 1, bits = 1
        else:
            mask_bits = 0
        
        frames = stream_bits - mask_bits + 1
         
        if mask_bits <= 1:            # case that we have a 1 or a 0
            frames = stream_bits - 3

        count = count_masked2( mask, bitstreamb, frames, stream_bits)


        #count = count_masked( mask, bitstreamb, bits)
        #mask_string = char
        print(f'{index}. {bitstreamb} contains 0x{mask1} {count} times')

if __name__ == "__main__":
    main()

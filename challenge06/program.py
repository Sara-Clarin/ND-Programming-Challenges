#!/usr/bin/env python3

# Sara Clarin
# Challenge06: find longest sequence of consecutive, distinct items in a list


import sys
fruitDict = {}
sequenceDict = {}

def retrieve_sequence( fruitDict):
    #seq_list = []
    #for fruit, val in sequenceDict.items():
     #   seq_list.append(fruit)

    possible_seq = tuple(fruitDict.keys())
    sequenceDict[possible_seq] = len(possible_seq)
    fruitDict.clear()

    #print( possible_seq)
    #return possible_seq


def find_distinct_fruits( line):
    sequence = []
    max_sequence = []
   
    count = 1
    for fruit in line:
        try:                    # we have a collision
            temp = fruitDict[fruit] 
            retrieve_sequence(fruitDict)
        
            #if len(sequence) > len(max_sequence):       # naively keeping track of maximum
                #max_sequence = sequence

            #fruitDict.clear()

        except KeyError:        # not yet seen
             fruitDict[fruit] = 0

    if len(fruitDict) > 0:
        retrieve_sequence( fruitDict)
        
    #sequenceDict.clear()
    #all_values = sequenceDict.values()
    #max_sequence = max(all_values)
    
    max_sequence = max(sequenceDict, key=sequenceDict.get)
    fruitDict.clear()
    sequenceDict.clear()
    return max_sequence


def main():

    for  line in sys.stdin.readlines():
       max_sequence = find_distinct_fruits( line.strip().split())
       l = len(max_sequence)
       print(f'{l}: {max_sequence}')


if __name__ == "__main__":
    main()

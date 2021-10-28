#!/usr/bin/env python3
import sys

PATH_COUNT = 0
tally = list()



  

def get_left( index, num_nodes):
    if 2*index + 1<= num_nodes:
        return 2*index + 1
    return -1

def get_right( index, num_nodes):
    if 2*index + 2 <= num_nodes:
        return 2*index + 2
    return -1



def XmasV3(  index , num_nodes, tree, target, tally, targvals):
        #base cases
        if index == -1:
            return

        if index >= num_nodes:
            return

        # recursive cases
        newtarget = []
        #print( f'Index: {index}, node: {tree[index]}') 
        node = tree[index]

        # check if we can start target over
        if target[0] == node:
            newtarget.append(1)

        for val in targvals:
            if val == len(target) - 1 and target[val] == node:
                tally.append( 1 )           # end of target and last char matches, increment counter

            elif target[val] == node:       # match in middle of target --> seek next char
                newtarget.append( val + 1 )      

        left = get_left( index, num_nodes)
        right = get_right(index, num_nodes)

        XmasV3( left, num_nodes, tree, target,  tally, newtarget)
        XmasV3( right, num_nodes, tree, target, tally, newtarget)


def main():
    for line in sys.stdin.readlines():
        target, tree = line.split()
        bin_target = str(bin( int(target))).lstrip('0b')
        n = len(tree)
        #print( target, tree, bin_target)
        #XmasTreePaths
        tally.clear()

        if target != '0' and target != '1':
        #print(bin_target.lstrip('0b'))
            #xmasv2( 0, n, tree, bin_target, 0, tally)
        #print(f"COUNT IS: {c}")

            targvals = [ ]
            XmasV3( 0, n, tree, bin_target, tally, targvals )
            print(f'Paths that form {target} in binary ({bin_target}): {len(tally)}')

        elif target == '1':
            print(f"Paths that form 1 in binary (1): {tree.count('1')}")

        else:
            print(f"Paths that form 0 in binary (0): {tree.count('0')}")
if __name__ == "__main__":
    main()
#!/usr/bin/env python3


import sys
import heapq
import collections


def read_graph(  m  ):
    '''
    graph: { node: {}}
    '''
    g = collections.defaultdict( list) # 
    print(f' in function')

    for _ in range( m):
        source, target = sys.stdin.readline().split()
        g[source].append(target)
        #print(source, target)
        g[target].append(source)
    print(' end of input')
    return g

def DFS_len( v , g):
    '''
    Depth-first search of an undirected graph, visiting an edge only once
    '''
    frontier = [ ]
    visited = { }
    frontier.append(v)
    pathcnt = 0

    while len(frontier) > 0:
        v = frontier.pop()
        print(f' v is: {v}')

        if v in visited:    # check to see if an edge was visited or not
            continue

        visited[v] = True  # add edge to visited list
        print(v)
        pathcnt += 1

        for u in g[v]:
            frontier.append( u)

    return pathcnt

def Compute_Longest( g ):
    '''
    call DFS-length on each node in the graph and return highest
    '''
    paths = 0
    print('in Compute_longest')
    first = list(g.keys())[0][0] 
    paths = DFS_len( first, g )

    return paths


def main():
    m = -1
    n = -1
    
    #sizes = sys.stdin.readline()

    while True:
        sizes = sys.stdin.readline()
        n, m = sizes.split()
        print(f'{m} {n}')

        if m == '0' and n == '0':
            print('breaking')
            break

        g = read_graph( int(m) )
        print(g)

        longest = Compute_Longest(g)
        print(longest)

if __name__ == "__main__":
    main()
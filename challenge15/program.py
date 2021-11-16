#!/usr/bin/env python3

# Sara Clarin
# 4 November 2021
# Longest Path problem: finds the longest path in undirected graph by 
# brute-force, recursive DFS

import sys
import collections

def read_graph(  m  ):
    '''
    input: number of edges in graph
    output: dictionary respresentation of adjacency list for undirected graph
    '''
    g = collections.defaultdict( list) # 

    for _ in range( m):
        source, target = sys.stdin.readline().split()
        g[source].append(target)
        g[target].append(source)
    
    return g

def vertices_to_edge( u, v):
    '''
    input: two vertices of graph (chars)
    output: a tuple with (v1, v2) in sorted order
    '''
    node_list = [u, v]
    n1 = sorted(node_list)
    return tuple( i for i in n1 )
            

def DFS_rec( cnt, g, node, visited, paths):

    for u in g[node]:
        edge = vertices_to_edge( u,  node)
        
        # base case
        if edge in visited:
            continue

        # recursive case  
        visited.add( edge)
        DFS_rec( cnt + 1, g, u, visited, paths)
        visited.remove(edge)
        
    paths.append(cnt)    
    return max( paths)

def Compute_Longest( g ):
    '''
    call DFS-length on each node in the graph and return highest
    '''
    
    max_path = 0
    for key in g.keys():
        max_path = max( max_path, DFS_rec( 0, g, key, set() , []) )
    
    return max_path


def main():
    m = -1
    n = -1
    
    while True:
        sizes = sys.stdin.readline()
        n, m = sizes.split()

        if m == '0' and n == '0':
            break

        g = read_graph( int(m) )
        print( Compute_Longest(g) )

if __name__ == "__main__":
    main()
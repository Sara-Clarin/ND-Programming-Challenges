#!/usr/bin/env python3


import sys, collections

def read_graph( ):
    '''
    graph: adjacency list for an undirected graph
    each vertex contains [ v1, v2 ....vn] neighbors
    N: number of vertices
    '''
    graph = collections.defaultdict( list )

    line = sys.stdin.readline().strip().split()
    start = 1

    while line[0] != '%':           # '%' is the sentinel value
        src,trg = map(int, line )
        
        graph[src].append( trg )
        graph[trg].append( src)
        line = sys.stdin.readline().strip().split()

    return graph, start

def hamilton_cycle( graph, start, vertex, visited, path, n):
    '''
    Brute force all hamiltonian cyclic paths via recursive DFS
    visited: set of nodes visited for backtracking
    path: ordered list of vertices in the current DFS path
    '''

    # base case: back at starting node, and visited 
    if len(path) == n:  
        if start in graph[vertex]:
            path.append(start)          
            return path
        else:
            return None

    # recursive step: backtrack if the path isn't what we want
    for neighbor in sorted(graph[vertex]):

        if neighbor in visited:
            continue

        visited.add( neighbor)
        path.append( neighbor)

        if hamilton_cycle( graph, start, neighbor, visited, path, n ):
            return path
    
        visited.remove( neighbor)
        path.pop(-1) 

        
def main():

    for n in sys.stdin:
        n = int(n.strip())
        graph, start = read_graph( )

        visited = set( )
        visited.add( start)
        path = []
        path.append(start)
        result = hamilton_cycle( graph, start, start, visited, path, n )
        
        if result:
            print(" ".join(  map(str, result))  )
        else:
            print('None')

if __name__ == "__main__":
    main()
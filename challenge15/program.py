#!/usr/bin/env python3


import sys
import heapq
import collections


def read_graph(  m  ):
    '''
    graph: { node: {}}
    '''
    g = collections.defaultdict( list) # 

    for _ in range( m):
        source, target = sys.stdin.readline().split()
        g[source].append(target)
        #print(source, target)
        g[target].append(source)
    
    return g

def vertices_to_edge( u, v):
    '''
    input: two vertices of graph (chars)
    output: a tuple with (v1, v2) in sorted order
    '''
    node_list = [u, v]
    n1 = sorted(node_list)
    #print('should print now')
    return tuple( i for i in n1 )


def DFS_len( v ,  g):
    '''
    Depth-first search of an undirected graph, visiting an edge only once
    idea: 
    '''
    frontier = [ ]
    visited = set()
    frontier.append(v)
    #frontier.append( edge)
    pathcnt = -1            # start with -1 so that first iteration counts first edge
    paths = []

    while len(frontier) > 0:
        v = frontier.pop()
        print(f' v is: {v}')

        #if edge in visited:    # check to see if an edge was visited or not
            #continue           # probably will delet

        #visited[edge] = True  # add edge to visited list
        
        pathcnt += 1
        children = 0

        for u in g[v]:
            edge = vertices_to_edge( u, v)

            if edge not in visited:  # only continue down edges we haven't seen yet
                #print(edge)
                visited.add( edge )
                frontier.append( u)
                children += 1
            #visited.remove(edge)   
            # we need to backtrack in here somewhere

        # idea: when we recurse back up, we subtract how far in we are
        if children == 0:
            paths.append(pathcnt)
            pathcnt = 0

    return max(paths)

def DFS_rec( cnt, g, node, visited, paths):

    for u in g[node]:
        edge = vertices_to_edge( u,  node)
        #print( edge )
        # base case: 
        if edge in visited:
            continue

        # recursive case
        else:
            visited.add( edge)
            DFS_rec( cnt + 1, g, u, visited, paths)
            visited.remove(edge)

    paths.append(cnt)
    # recursive step: visit adjacent nodes
    
    return max( paths)

def Compute_Longest( g ):
    '''
    call DFS-length on each node in the graph and return highest
    '''
    
    first_v = list(g.keys())[0][0]
    second = list(g.values())[0][0]
    #first_e = (first_v, second)
    #print(first_e)

    # for key, val in g.items():
    #paths = DFS_len( first_v,    g )
    max_path = 0
    for key in g.keys():
        max_path = max( max_path, DFS_rec( 0, g, key, set() , []) )
    
    return max_path


def main():
    m = -1
    n = -1
    
    #sizes = sys.stdin.readline()

    while True:
        sizes = sys.stdin.readline()
        n, m = sizes.split()
        #print(f'{m} {n}')

        if m == '0' and n == '0':
            break

        g = read_graph( int(m) )
        #print(g)

        #print(f'Sorting edges :))')
        #print( vertices_to_edge( m, n))

        print( Compute_Longest(g) )
        #print(f'longest path: {longest}')

if __name__ == "__main__":
    main()
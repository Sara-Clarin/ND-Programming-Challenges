#!/usr/bin/env python3


import sys, collections

def read_graph( N):
    '''
    graph: adjacency list for an undirected graph

    '''
    graph = collections.defaultdict( dict )

    line = sys.stdin.readline().strip().split()
    #src, trg = map(int, line)
    #print(f'first line: {line}')
    start = int(line[0])

    edge_id = 0
    while line[0] != '%':
        #print(line)
        src,trg = map(int, line )
        
        graph[src][trg] = edge_id
        graph[trg][src] = edge_id
        edge_id += 1

        line = sys.stdin.readline().strip().split()

    #print(f' next graph: ')
    return graph, start

def hamilton_cycle( graph, start, vertex, visited, path, n):
    '''
    Brute force all cyclic paths via recursive DFS
    '''
    #visited = collections.defaultdict( int)
    #visited[vertex] 
    #visited[vertex] +=  1

    # base case: back at starting node, and visited 
    if len(visited) == n and path[-1] == start: #visited[vertex] == 2 #and len(visited.keys()) == n: 
        return path

    # recursive step: backtrack if the path isn't what we want

    for neighbor in graph[vertex]:

        if neighbor in visited:
            continue

        visited.add( neighbor)
        path.append( neighbor)
        #print(f'path: {path}')

        if hamilton_cycle( graph, start, neighbor, visited, path, n ):
            return path
        
        # backtrack: pretend this is new starting point
        #newvisited = set()
        #newpath = []
        #path.clear()
        #hamilton_cycle( graph, neighbor, newvisited, newpath, n)
    
        visited.remove( neighbor)
        path.pop(-1) 


def main():

    for n in sys.stdin:
        n = int(n.strip())
        graph, start = read_graph( n )
        #print(f'{graph}')

        #visited = collections.defaultdict( int )
        visited = set( )
        path = []
        #path.append(start)
        #visited.add( start)
        result = hamilton_cycle( graph, start, start, visited, path, n )

        if result:
            result.insert(0, start)
            print(" ".join(  map(str, result))  )
        else:
            print('None')

        graph.clear()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys, collections


def read_graph( connections):
    graph = collections.defaultdict(dict)

    for _ in range(connections):
        s, t, w = map( int, sys.stdin.readline().strip().split())
        
        graph[s][t] = graph[s].get(t, 0) + w
        graph[t][s] = graph[t].get(s, 0) + w

    return graph

def find_bfspath( graph, start, weight, sink):
    '''

    '''
    visited = { }
    #frontier = [ src]  # use "queue" for BFS traversal
    frontier = collections.deque(  )
    frontier.append( (start, start, weight))
    src = 1
    trg = 1
    path = []

    #print(f'frontier: {frontier[0]}')
    while frontier:
        src, trg, weight = frontier.popleft()
        #w = frontier.popleft()
        #print(w)
        if trg in visited:
            continue

        if trg == sink: 
            visited[sink] = src
            #visited[src] = sink
            #print( sink)
            break

        #print(src, trg, weight) 
        visited[trg] = src

        for neighbor, capacity in graph[trg].items():
            if capacity > 0:
                frontier.append( ( trg, neighbor , capacity ))

    if sink in visited:             # if we can't get to the sink, we've traversed all src-->sink paths
        return visited
    else:
        return None

def compute_min_flow( graph, visited, start, sink ):
    path = []
    min_cost = sys.maxsize
    curr = sink
    path.append( sink)

    while curr != start:
        next = visited[curr]
        if graph[curr][next] < min_cost:
            min_cost = graph[curr][next]
        curr = next
        path.append( curr)

    path.reverse()
    #print(f'{path} has min flow {min_cost}')
    return path, min_cost

def reduce_capacity( graph, path, min_flow):
    '''
    Go through every pair of adjacent nodes in path
    decrement the edge weight by min_flow
    '''

    for i in range( 1, len( path)):
        src, trg = path[i], path[ i-1]
        #print(src, trg)
        graph[src][trg] -= min_flow
        graph[trg][src] -= min_flow

    #print(f' Graph decremented: {graph}')
    return graph

def main():
    '''
    visited = { 1 }
    for n in sys.stdin:

        n = int(n.strip())
        if n == 0:
            break
        src, trg, connections = map(int, sys.stdin.readline().strip().split())
        print(n, src, trg, connections)
      
        graph = read_graph( connections )
        print(graph)
        visited = find_dfspath( graph, src, 0, trg )
     '''
    n = int(sys.stdin.readline().strip() )
    src, sink, connections = map(int, sys.stdin.readline().strip().split())
    visited = { }
    iterations = 0
    
    #while visited or iterations == 0 or iterations < 10:
    while True:
        graph = read_graph(connections)
        visited = find_bfspath( graph, src, 0, sink )
        bandwidth = 0
        #print(f'visited: {visited}')

        while visited:  
            #print(graph)

            path, minimum_flow = compute_min_flow( graph, visited, src, sink)
            graph = reduce_capacity( graph, path, minimum_flow) 
            visited = find_bfspath( graph, src, 0, sink )

            #print(f'visited: {visited}')  
            bandwidth += minimum_flow

        iterations += 1
        print(f'Network {iterations}: Bandwidth is {bandwidth}.')

        n = int(sys.stdin.readline().strip() )
        if n == 0:
            break
        src, sink, connections = map(int, sys.stdin.readline().strip().split())

        

if __name__ == "__main__":
    main()
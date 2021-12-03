#!/usr/bin/env python3


# Maximum Bandwidth: a program that determines the maximum flow of an undirected graph
# 18 November 2021


import sys, collections


def read_graph( connections):
    '''
    Create a weighted graph with n connections from stdin
    '''
    graph = collections.defaultdict(dict)

    for _ in range(connections):
        s, t, w = map( int, sys.stdin.readline().strip().split())
        
        graph[s][t] = graph[s].get(t, 0) + w
        graph[t][s] = graph[t].get(s, 0) + w

    return graph

def find_bfspath( graph, start, weight, sink):
    '''
    Iterative BFS traversal from start --> sink
    '''
    visited = { }
    frontier = collections.deque(  )
    frontier.append( (start, start, weight))

    while frontier:
        src, trg, weight = frontier.popleft()

        if trg in visited:
            continue

        if trg == sink: 
            visited[sink] = src
            break

        visited[trg] = src

        for neighbor, capacity in graph[trg].items():
            if capacity > 0:
                frontier.append( ( trg, neighbor , capacity ))


    if sink in visited:             # if we can't get to the sink, we've traversed all src-->sink paths
        return visited
    else:
        return None

def compute_min_flow( graph, visited, start, sink ):
    '''
    Traverse visited from sink --> start and record the most recent path
    Find the bottleneck point along the path ( min_cost)
    '''
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
    return path, min_cost

def reduce_capacity( graph, path, min_flow):
    '''
    Go through every pair of adjacent nodes in path
    Decrement the edge weight by bottleneck weight
    '''

    for i in range( 1, len( path)):
        src, trg = path[i], path[ i-1]
        graph[src][trg] -= min_flow
        graph[trg][src] -= min_flow

    return graph

def main():

    # INITIAL CONDITIONS
    n = int(sys.stdin.readline().strip() )
    src, sink, connections = map(int, sys.stdin.readline().strip().split())
    visited = { }
    iterations = 0
    
    while True:
        graph = read_graph(connections)
        visited = find_bfspath( graph, src, 0, sink )
        bandwidth = 0

        while visited:  
            path, minimum_flow = compute_min_flow( graph, visited, src, sink)
            graph = reduce_capacity( graph, path, minimum_flow) 
            visited = find_bfspath( graph, src, 0, sink )
            bandwidth += minimum_flow

        iterations += 1
        print(f'Network {iterations}: Bandwidth is {bandwidth}.')

        n = int(sys.stdin.readline().strip() )
        if n == 0:
            break
        src, sink, connections = map(int, sys.stdin.readline().strip().split())

if __name__ == "__main__":
    main()
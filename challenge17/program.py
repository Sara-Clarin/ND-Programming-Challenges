#!/usr/bin/env python3

# Sim City: program to find the minimum fully-connecting path (minimum spanning tree) between points on the coordinate plane

import sys, collections, math, heapq


def Make_Graph( N):
    g = collections.defaultdict( dict)
    vertices = []

    for i in range(N):
        pair = sys.stdin.readline().strip()
        #X, Y = map(float, pair.split())
        vertices.append(pair)

    for i,v in enumerate(vertices):
        X1, Y1 = map(float, v.split())
        if i < N -1:
            others = vertices[i+1:]
        
            #print(f'{X1}{Y1}, {others}')
            for other in others:
                X2, Y2 = map(float, other.split())
                dist = math.sqrt( (X1-X2)**2 + (Y1-Y2)**2 )
                g[ v] [other] = dist
                g[ other] [v] = dist   

        #g[X][Y] = dist
        #g[Y][X] = dist
        #print(X, Y)

    #print(g)
    return g, pair

def min_spanning_tree(g, start):
    visited = {}
    frontier = []

    heapq.heappush( frontier, (0, start, start))

    while frontier:
        distance, source, target = heapq.heappop(frontier)

        if target in visited:
            continue

        visited[target] = source

        for neighbor, dist in g[target].items():
            heapq.heappush(frontier, (dist, target, neighbor) )

    return visited

def get_cost( visited, g):
    '''
    Compute the cost of the MST from Prim's algorithm
    idea: the MST will cover all the vertices. if we have a list of all the verti
    fact: one node could be connected to multiple vertices (it's not a straight path)
    if source == target then cost += 0
    else get cost from g[source], [target]. should be same as g[target][source]
    '''
        
    vertices = set(visited.keys()  )
    traversed = {} 
    curr = g[0][0]
    cost = 0

    while traversed != vertices:
        next = visited[curr]
        cost += g[curr][next]
        curr = next

    return cost
def get_costv2(visited, g):
    cost = 0
    for source, target in visited.items():
        if source != target:
            cost += g[source][target]

    return cost

def main():

    while True:
        line = sys.stdin.readline()
        N = list(map(int, line.split()))[0]
        
        if N == 0:
            break
        g, start = Make_Graph( N )
        #print(f'start: {start}')

        visited = min_spanning_tree( g, start)
        #print(visited)
        print(f'{get_costv2(visited, g):.2f}')
        #get_cost(visited)
        

if __name__ == "__main__":
    main()
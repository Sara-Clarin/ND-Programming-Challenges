#!/usr/bin/env python3

import sys, collections

#class Graph:
    #edges : collections.defaultdict(set)
    #degrees: collections.defaultdict(int)
Graph = collections.namedtuple( "Graph", "edges degrees")

def make_graph():
    '''
    Creates a (directed) dependency graph out of trigram input sequences.
    '''
    edges = collections.defaultdict(set)
    degrees = collections.defaultdict(int)

    for line in sys.stdin:
        first, second, third = map(int, line.strip())
        #print(second)

        if second not in edges[first]:
            degrees[second] += 1

        if third not in edges[second]:
            degrees[third] += 1


        edges[first].add(second)  # source (first) --> target (second)
        #edges[first].add(third)
        edges[second].add(third)

        #degrees[third] += 1

        degrees[first]   # if first never before referenced, add entry deg(first) = 0


    #for target, sources in edges.items():
        #degrees[target] = len(sources)

    #print( edges)
    #print( degrees)
    return Graph(edges, degrees)

def topological_sort( graph):

    visited = []
    frontier = [  v for v,d in graph.degrees.items() if d == 0 ]

    while frontier:
        vertex = frontier.pop()

        visited.append(vertex)  # visit the vertex

        for neighbor in graph.edges[vertex]:
            graph.degrees[neighbor] -= 1

            if graph.degrees[neighbor] == 0:
                frontier.append(neighbor)

    return visited

def main():

    
    graph = make_graph()
    
    #print( graph.edges )
    visited = topological_sort( graph )
    print( "".join(str(i) for i in visited))
    

if __name__ == "__main__":
    main()
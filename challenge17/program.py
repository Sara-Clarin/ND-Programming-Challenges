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

        edges[second].add(first)  # source (first) --> target (second)
        edges[third].add(second)

        degrees[second] += 1
        degrees[third] += 1

        degrees[first]   # if first never before referenced, add entry deg(first) = 0
    
    print( edges)
    print( degrees)
    return Graph(edges, degrees)

def topological_sort( graph):

    visited = []
    frontier = [  v for v,d in graph.degrees.items() if d == 0 ]


    return visited

def main():


    graph = make_graph()
    print( graph)
    #print( graph.edges )


if __name__ == "__main__":
    main()
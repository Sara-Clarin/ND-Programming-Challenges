#!/usr/bin/env python3
import sys
from dataclasses import dataclass
import collections
import heapq

@dataclass
class Cell:
    id : int

def getID( row, col, COLS):
    return row*COLS + col

def Get_Matrix( row, col):
    ''' create a matrix representation of input
    iterate through the matrix to make undirected graph
    maybe our matrix will store the ID at a cell if it's not 1
    # in iteration, we'll calculate cell's costs
    # graph:  ID : { neighborID: cost, NeighborID2: cost2 }
    # output: graph, start, end[]
    '''
    CLOSED = 1000
    start = 0
    end = []

    matrix = [ [0 for i in range(col ) ] for i in range(row) ]

    for i in range(row ):
        rowlist = sys.stdin.readline()
        rowlist = rowlist.split()
        #print(rowlist)

        for j in range(col ):
            if rowlist[j] == 'S':          # set start and end variables
                start = getID(i,j,col)
                matrix[i][j] = start
            elif rowlist[j] == 'E':
                #print("adding the end val")
                end.append( getID(i,j,col))
                matrix[i][j] = getID(i, j, col)  # change this so 1 function call
            elif rowlist[j] != '1':
                matrix[i][j] = getID(i, j, col)
            else:
                matrix[i][j] = CLOSED
        
    # pad the left with sentinels
    for i in range(row):
        matrix[i].insert( 0,-50 )

    matrix.insert(0, [ -50 for i in range(col + 1) ])
    #print( matrix)
    #print(f'END in function: {end}')
    return start, end, matrix
    
def Matrix_to_adjList( matrix, row, col):

    g = collections.defaultdict(dict)
    CLOSED = 1000
    #print(matrix)

    for i in range(1, row  + 1):    
        for j in range(1,col + 1 ):
            #print(f'cell : {matrix[i][j]}')
            cell = matrix[i][j]
            if cell == CLOSED:
                continue
        
            # 4 NONDIAGONAL DIRECTIONS: weight = 1
            # top
            if matrix[ i - 1][j] != -50 and matrix[i - 1][j] != CLOSED: 
                #print(f"top exists: {matrix[i-1][j]}")
                top = matrix[i - 1][j]
                g[ cell ][ top] = 1         # g[src][trget] = wt
                g[top][cell] = 1
            # bottom
            if i != row and matrix[i + 1][j] != CLOSED:
                #print(f"bottom exists: {matrix[i + 1][j]}")
                bottom = matrix[i+1][j]
                g[cell][bottom] = 1
                g[bottom][cell] = 1
            # right
            if j != col and matrix[i][j+1] != CLOSED:
                #print(f"right exists: {matrix[i][j + 1]}")
                right = matrix[i][j + 1]
                g[cell][right] = 1
                g[right][cell] = 1
            # left
            if j != 1 and matrix[i][j - 1] != CLOSED:
                #print(f"left exists: {matrix[i][j - 1]}")
                left = matrix[i][j -1]
                g[cell][left] = 1
                g[left][cell] = 1

            # 4 DIAGONAL DIRECTIONS: weight = 2
            # topleft
            if matrix[i - 1][j - 1] != -50 and matrix[i-1][j-1] != CLOSED:
                toplft = matrix[i-1][j-1]
                g[cell][toplft] = 2
                g[toplft][cell] = 2
            # topright
            if j != col and matrix[i-1][j +1] != CLOSED and matrix[i-1][j+1] != -50:
                toprt = matrix[i-1][j+1]
                g[cell][toprt] = 2
                g[toprt][cell] = 2
            # bottom left
            if i != row and matrix[i+1][j-1] != -50 and matrix[i+1][j-1] != CLOSED:
                botleft = matrix[i+1][j-1]
                g[cell][botleft] = 2
                g[botleft][cell] = 2
            # bottom right
            if i != row and j != col and matrix[i+1][j+1] != CLOSED:
                botright = matrix[i+1][j+1]
                g[cell][botright] = 2
                g[botright][cell] = 2

    #print(g)
    return g

def compute_sssp( g, start, end):

    frontier = []   # nodes reachable but not visited
    visited = {}    # nodes we've visited : weights
    distance = 0

    heapq.heappush( frontier, (0, start, start))

    while frontier:
        distance, source, target = heapq.heappop(frontier)

        if target in visited: 
            continue

        visited[target] = source
        #visited[target] = (source, distance)
        #visited[target][source] = distance

        #if target == end:  
            #print(f'end: {end}') 
            #break

        for neighbor, weight in g[target].items(): 
            heapq.heappush( frontier, (distance + weight, target, neighbor ))

    return visited

def Reconstruct_Path( graph, visited, source, target ):

    #print(f'visited: {visited}')
    path = []
    curr = target
    cost = 0

    while curr != source:
        path.append(curr)
        try:
            next = visited[curr]
            cost += graph[curr][next]
            curr = next
        except KeyError:
            #print(f"Key error!!! {curr}")
            return 0, []
    
    #print(f'Cost: {cost}')
    path.append(source)
    path.reverse()
    #print(f'Path: {path}')
    return cost, path

def main():

    r = -1
    c = -1

    while True:
        line = sys.stdin.readline()
        r, c = map(int, line.split())

        if r == 0 and c == 0:
            break

        start, end, matrix = Get_Matrix( r, c )
        #print(f'START: {start} END: {end}')
        #print(f'END: {end}')
        g = Matrix_to_adjList( matrix, r, c )

        mincost = sys.maxsize
        minpath = []
        for e in end:
            visited = compute_sssp(g, start, e)
            cost, path = Reconstruct_Path( g, visited, start, e)
            if cost < mincost and cost != 0:
                mincost = cost
                minpath = path

        if len(minpath) > 0:
            print(f'Cost: {mincost} Path: {" ".join(str(i) for i in minpath)}')
        else:
            print(f'Cost: 0 Path: None')
        
        
if __name__ == "__main__":
    main()



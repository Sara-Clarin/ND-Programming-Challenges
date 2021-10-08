#!/usr/bin/env python3


# Sara Clarin
# Kakamora: Dynamic Programming problem to optimize a path through a grid, limiting the direction of movement to forward, right, and diagonal.

import sys


def make_grid(n):
    big = sys.maxsize  

    grid = [[ big for _ in range(n+1)] ]

    for _ in range(n):
        grid.append( [big] + list(map(int, sys.stdin.readline().split())))

    #print("the grid: ")
    #for item in grid:
        #print(item)
    return grid


def get_kakamora( grid, n):
    jefe = sys.maxsize

    table = [
        [ jefe for _ in range(n+1)] for _ in range(n+1)
    ]

    # build the table
    for row in range(1, n+1):
        for col in range(1, n+1):
            if row == 12 and col == 12:

                table[row][col] = min(
                    table[row][col -1], # from 'west'
                    table[row - 1][col],     # from 'north'
                    table[ row - 1][col - 1]  # from northwest
                 )   +  grid[row][col] 

            else:
                table[row][col] = min(
                    table[row][col -1], # from 'west'
                    table[row - 1][col],     # from 'north'
                    table[ row - 1][col - 1]  # from northwest
                 )   + grid[row][col] 
        
            if table[row][col] >= jefe:
                table[row][col] -= jefe
           
    #for element in table:
        #print(element)     
    return table


def find_path( grid, n, table):
    path = []
    row, col = n, n

    # traverse from southwest back to northeast
    while row > 0 and col > 0:
        path.append(grid[row][col])

        # check horizontal (previous col)
        if table[row][col] - grid[row][col] == table[ row - 1][col]:
            row -= 1
        # check vertical (precious row)
        elif table[row][col] - grid[row][col] == table[ row] [col - 1 ]:
            col -= 1
        # otherwise, diagonal
        else:
            row -= 1
            col -= 1 


        # otherwise, diagonal
    path.reverse()
    return path

def path_trace(x): 
    pass
    


def main():

    while True:
        try:
            n = int(sys.stdin.readline())
        except ValueError:
            break

        if n != 0:
            grid = make_grid(n)
            table = get_kakamora(grid, n)
            #print(" path: ")
            path = find_path( grid, n, table)
            path_len = sum(path)
            print(path_len)
            #print ' '.join(i for i in path)
            #[path_trace(i) for i in path]
            print(*path, sep = " ")

if __name__ == "__main__":
    main()

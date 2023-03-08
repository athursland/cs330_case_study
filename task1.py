"""
case study task 3
ali mike dylan and noa
"""

import csv
import math
import random
import collections
import sys
import statistics
#import matplotlib
import heapq

### define global variables
filename = 'geolife-cars-ten-percent.csv'
data = []
r = 1
grid = None

def import_data(fname):
    """
    import data from csv
    """
    global data

    with open(fname, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None) # skip the headers
        for row in reader:
            x = float(row[2])
            y = float(row[3])
            data.append((x, y))

def get_cell_indices(point):
    """
    helper function for preprocess - 
    given a point p, decide which cell it belongs in
    """
    col = int(point[0]-minx / r)
    row = int(point[1]-miny / r)
    return col, row

def preprocess(data):
    """
    using the input data, find the optimal value of r
    to be used for pre-processing (creating the grid)
    O (n log n) time for sorting
    """
    global minx, maxx, miny, maxy
    minx = min(point[0] for point in data)
    maxx = max(point[0] for point in data)
    miny = min(point[0] for point in data)
    maxy = max(point[1] for point in data)
    print("minx", minx)
    print("maxx", maxx)
    print("miny", miny)
    print("maxy", maxy)

    # define width and height of our plane (based on input)
    width = abs(maxx - minx)
    height = abs(maxy - miny)
    
    # define number of columns and rows for our grid 
    global num_cols
    global num_rows
    num_cols = int(width / r) + 1
    num_rows = int(height / r) + 1
    print(num_cols)
    print(num_rows)

    # initialize an empty grid with the appropriate number of cells
    global grid 
    grid = [[[] for _ in range(num_cols)] for _ in range(num_rows)]

    for point in data: 
        col, row = get_cell_indices(point)
        #print("col: ", col)
        #print("row: ", row)
        grid[row][col].append(point)

    for row in grid:
        for cell in row:
            #print("flag2")
            cell.sort()

def density(p):
    """
    find the density for a given point
    input: p, a point that may or may not be in P
    output: the # of points within r*r square of p
    ~O(1) time
    """
    col, row = get_cell_indices(p)

    # add everything in the given cell to ret
    count = len(grid[row][col])

    # now check adjacent cells
    if row > 1: # row is not last
        count += len([q for q in grid[row-1][col] if q[1] <= (p[1] + r)])
    if row < len(grid): # row is not last 
        count += len([q for q in grid[row+1][col] if q[1] >= (p[1] - r)])
    if col > 1: # col is not first 
        count += len([q for q in grid[row][col-1] if q[0] >= (p[0] - r)])
    if col < len(grid[0]): # col is not last
        count += len([q for q in grid[row][col+1] if q[0] <= (p[0] + r)])

    return count

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

def hubs(k):
    """
    identify k > - hubs of high density s.t. 
    any two hubs re separated by at least distance r
    O(n) runtime complexity 
    """
    # each item in the heap is a tuple of where 0 = density and 1 = coordinates
    ret = [(0, (0,0))] * k # initialize list of 0s of length k
    print("ret: ", ret)
    heapq.heapify(ret) # make it a heap 

    print("hubs flag")
    upper_bound = maxy
    for row in range(num_rows):
        left_bound = minx
        print("row: ", row)
        for col in range(num_cols):
            print("col: ", col)
            # get the center of the given cell
            cell_center = (((left_bound*2 + r)/2), (upper_bound*2 - r)/2)
            print("cell_center x: ", cell_center[0])
            print("cell_center y: ", cell_center[1])
            print("grid cell: ", grid[row][col])
            if density(cell_center) > min(ret, key = lambda x: x[0]):
                heapq.heapreplace(ret, (density(cell_center), cell_center))
            
            left_bound += r # increment left bound by r
        upper_bound -= r # decrement upper bound by r
        # so we are moving to the right across the grid, and moving down

    return ret

def visualize():
    """
    visualize
    """
    return 


def main():
    """
    main function
    1. import the data from csv file 
    2. pre-process the data
    3. call density
    4. call hubs
    """
    import_data(filename) # step 1
    preprocess(data) # step 2

    p = random.choice(data)
    print("random point: ", p)
    print("number of points: ", len(data))
    print("density of p: ", density(p))
    return hubs(4)

if __name__ == "__main__":
    print(main())
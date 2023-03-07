"""
case study task 3
ali mike dylan and noa
"""

import csv
import math
import collections
import sys
import statistics

### define global variables
filename = 'geolife-cars-ten-percent.csv'
data = []
r = 1
grid = None
DENOM = 20

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
    minx = min(point[0] for point in data)
    miny = min(point[1] for point in data)
    col = int(point[0]-minx / r)
    row = int(point[1]-miny / r)
    return col, row

def preprocess(data):
    """
    using the input data, find the optimal value of r
    to be used for pre-processing (creating the grid)
    O (n log n) time for sorting
    """
    # define width and height of our plane (based on input)
    width = abs(max(point[0] for point in data) - min(point[0] for point in data))
    height = abs(max(point[1] for point in data) - min(point[0] for point in data))

    # define number of columns and rows for our grid 
    num_cols = int(width / r)
    num_rows = int(height / r)

    # initialize an empty grid with the appropriate number of cells
    global grid 
    grid = [[[] for _ in range(num_cols)] for _ in range(num_rows)]

    for point in data: 
        col, row = get_cell_indices(point)
        grid[row][col].append(point)

    for row in grid:
        for cell in row:
            print("flag2")
            cell.sort()

def density(p):
    """
    find the density for a given point
    """
    cell = get_cell_indices(p)

    return len(cell)

def hubs(k, r):
    """
    identify k > - hubs of high density s.t. 
    any two hubs re separated by at least distance r
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
    print(grid)
    return preprocess(data) # step 2

if __name__ == "__main__":
    print(main())
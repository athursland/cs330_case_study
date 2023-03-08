"""
case study task 3
ali mike dylan and noa
"""

import csv
import random
import heapq
import time 

### define global variables
ten_percent = 'geolife-cars-ten-percent.csv'
thirty_percent = 'geolife-cars-thirty-percent.csv'
sixty_percent = 'geolife-cars-sixty-percent.csv'
full_dataset = 'geolife-cars.csv'
data = []
r = 5
grid = None

interval = 0

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
    #print("get cell indices flag!!!!")
    col = int((point[0]-minx) / r)
    row = int((point[1]-miny) / r)
    #print("col: ", col)
    #print("row: ", row)
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
    miny = min(point[1] for point in data)
    maxy = max(point[1] for point in data)

    # define width and height of our plane (based on input)
    width = abs(maxx - minx)
    print("width: ", width)
    height = abs(maxy - miny)
    print("height: ", height)
    
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
        print("col: ", col)
        print("row: ", row)
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
    #print("density flag!!!!!")
    col, row = get_cell_indices(p)
    #print("row: ", row)
    #print("col: ", col)

    # add everything in the given cell to ret
    count = len(grid[row][col])

    # now check adjacent cells
    if row > 1: # row is not last
        count += len([q for q in grid[row-1][col] if q[1] <= (p[1] + r)])
    if row+1 < len(grid): # row is not last 
        count += len([q for q in grid[row+1][col] if q[1] >= (p[1] - r)])
    if col > 1: # col is not first 
        count += len([q for q in grid[row][col-1] if q[0] >= (p[0] - r)])
    if col+1 < len(grid[0]): # col is not last
        count += len([q for q in grid[row][col+1] if q[0] <= (p[0] + r)])

    return count

def hubs(k):
    """
    identify k > - hubs of high density s.t. 
    any two hubs re separated by at least distance r
    O(n) runtime complexity 
    """
    start = time.time()
    # each item in the heap is a tuple of where tup[0] = density and tup[1] = coordinates (x,y)
    ret = [(0, (0,0))] * k # initialize list of 0s of length k
    #print("ret: ", ret)
    heapq.heapify(ret) # make it a heap 

    #print("hubs flag")
    upper_bound = maxy
    for row in range(num_rows):
        left_bound = minx
        #print("row: ", row)
        for col in range(num_cols):
            #print("col: ", col)
            cell_center = (((left_bound*2 + r)/2), (upper_bound*2 - r)/2) # get the center of the cell
            """
            print("cell_center x: ", cell_center[0])
            print("cell_center y: ", cell_center[1])
            print("grid cell: ", grid[row][col])
            print("conditional flag!!!!")
            """
            if density(cell_center) > min(ret, key = lambda x: x[0])[0]:
                heapq.heapreplace(ret, (density(cell_center), cell_center))
            
            left_bound += r # increment left bound by r
        upper_bound -= r # decrement upper bound by r
        # so we are moving to the right across the grid, and moving down

    end = time.time()

    global interval 
    interval = end - start

    return ret
    
if __name__ == "__main__":
    
    ### 10% 
    import_data(ten_percent) # step 1
    preprocess(data) # step 2
    p = random.choice(data)
    print(hubs(10))
    print("points in dataset: ", len(data))
    print("10% time: ", interval)
    """
    ### 30% 
    data = []
    import_data(thirty_percent) # step 1
    preprocess(data) # step 2
    p = random.choice(data)
    print(hubs(2))
    print("points in dataset: ", len(data))
    print("30% time: ", interval)

    ### 60%
    data = []
    import_data(sixty_percent) # step 1
    preprocess(data) # step 2
    p = random.choice(data)
    print(hubs(2))
    print("points in dataset: ", len(data))
    print("60% time: ", interval)

    ### full dataset
    data = []
    import_data(full_dataset) # step 1
    preprocess(data) # step 2
    p = random.choice(data)
    print(hubs(2))
    print("points in dataset: ", len(data))
    print("100% time: ", interval)
    """
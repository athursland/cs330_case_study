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
filename = 'geolife-cars.csv'
raw_data = []

class TreeNode: 
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.density = None
        self.left = None
        self.right = None
    
def insert_x(root, id, x, y):
    """
    insert new node into tree based on x value
    """
    if root is None: 
        root = TreeNode(id, x, y)
        return root
    if x < root.x:
        root.left = insert_x(root.left, id, x, y)
    else:
        root.right = insert_x(root.right, id, x, y)
    return root
    
def insert_y(root, id, x, y):
    """
    insert new node into tree based on y value
    """
    if root is None: 
        root = TreeNode(id, x, y)
        return root
    if x < root.y:
        root.left = insert_y(root.left, id, x, y)
    else:
        root.right = insert_y(root.right, id, x, y)
    return root

def import_data(fname):
    """
    import data from csv
    """
    with open(fname, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None) # skip the headers
        for row in reader:
            id = row[1]
            print(row[2])
            print(row[3])
            x = float(row[2])
            y = float(row[3])
            raw_data.append((id, x, y))

def main():
    """
    main function
    1. import the data from csv file 
    2. create and populate x_bst - during insertion, update density
    3. create and populate y_bst
    4. for a given r, calculate 
    """
    x_bst = None
    y_bst = None
    import_data(filename)
    x_median = median()

if __name__ == "__main__":
    print(main())
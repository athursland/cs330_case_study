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

class Node: 
    def __init__(self, id, x, y):
        self.id = id # unique id
        self.x = x # x-coord
        self.y = y # y-coord 
        self.size = 1 # size of subtrees below
        self.left = None
        self.right = None

class BST:
    """
    BST class, where insert is sorted by 
    """
    def __init__(self):
        self.root = None

    ### ALL THE X METHODS: search, insert

    def x_search(self, node):
        """
        search for a given point based on id field
        """
        if self.root is None or self.root.id == node.id: # base case
            return self.root
        
        # node has a greater x value than root
        if self.root.x < node.x:
            return self.search(self.root.right, node)
        
        # node has a smaller or equal x value than root
        return self.search(self.root.left, node)
        
    def x_add(self, point):
        node = Node(point[0], point[1], point[2])
        self.x_insert(self.root, node)
    
    def x_insert(self, root, node):
        if root == None:
            self.root = node
        else:
            root.size += 1 
            if root.x > node.x:
                if root.left == None:
                    root.left = node
                else:
                    self.x_insert(root.left, node)
            else: # is root.x == node.x we insert node into the right subtree
                if root.right == None:
                    root.right = node
                else:
                    self.x_insert(root.right, node)

    ### ALL THE Y METHODS: search, insert

    def y_add(self, point):
        """
        insert row into BST based on y-value of p 
        """
        node = Node(point[0], point[1], point[2])
        self.y_insert(self.root, node)
    
    def y_insert(self, root, node):
        if root == None:
            self.root = node
        else:
            root.size += 1 
            if root.y > node.y:
                if root.left == None:
                    root.left = node
                else:
                    self.y_insert(root.left, node)
            else: # if root.y == node.y we insert node into the right subtree
                if root.right == None:
                    root.right = node
                else:
                    self.y_insert(root.right, node)

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

def density(point, r):
    """
    find the density for a given point
    """
    return

def main():
    """
    main function
    1. import the data from csv file 
    2. create and populate x_bst - during insertion, update density
    3. create and populate y_bst
    4. for a given r, calculate 
    """
    import_data(filename)
    x_bst = BST()
    y_bst = BST()

    for row in raw_data:
        x_bst.x_add(row)
        y_bst.y_add(row)

    return(x_bst.root.id, y_bst.root.id)

if __name__ == "__main__":
    print(main())
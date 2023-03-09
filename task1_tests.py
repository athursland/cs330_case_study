"""
tests for task1
"""

import task1
import time

### globals
global data
global interval

def test_ten():
    task1.data = []
    start = time.time()
    task1.import_data('geolife-cars-ten-percent.csv')
    task1.preprocess(task1.data)
    end = time.time()
    print("points in dataset: ", len(task1.data))
    print("10% time: ", (end-start))

def test_thirty():
    task1.data = []
    start = time.time()
    task1.import_data('geolife-cars-thirty-percent.csv')
    task1.preprocess(task1.data)
    end = time.time()
    print("points in dataset: ", len(task1.data))
    print("30% time: ", (end-start))

def test_sixty():
    task1.data = []
    start = time.time()
    task1.import_data('geolife-cars-sixty-percent.csv')
    task1.preprocess(task1.data)
    end = time.time()
    print("points in dataset: ", len(task1.data))
    print("60% time: ", (end-start))

def test_full():
    task1.data = []
    start = time.time()
    task1.import_data('geolife-cars.csv')
    task1.preprocess(task1.data)
    end = time.time()
    print("points in dataset: ", len(task1.data))
    print("100% time: ", (end-start))

if __name__=="__main__":
    test_ten()
    test_thirty()
    test_sixty()
    test_full()
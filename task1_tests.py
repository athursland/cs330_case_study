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
    task1.hubs(10, 8)
    end = time.time()
    return (end-start)

def test_thirty():
    task1.data = []
    start = time.time()
    task1.import_data('geolife-cars-thirty-percent.csv')
    task1.preprocess(task1.data)
    task1.hubs(10, 8)
    end = time.time()
    return (end-start)

def test_sixty():
    task1.data = []
    start = time.time()
    task1.import_data('geolife-cars-sixty-percent.csv')
    task1.preprocess(task1.data)
    task1.hubs(10, 8)
    end = time.time()
    return (end-start)

def test_full():
    task1.data = []
    start = time.time()
    task1.import_data('geolife-cars.csv')
    task1.preprocess(task1.data)
    task1.hubs(10, 8)
    end = time.time()
    return (end-start)

def hubs_test(k, r):
    times = []
    start = time.time()
    task1.import_data('geolife-cars-ten-percent.csv')
    task1.preprocess(task1.data)
    task1.hubs(k, r)
    end = time.time()
    return (end-start)

if __name__=="__main__":
    file1 = open('task1_tests.txt', 'w')
    results = []
    results.append("10%: " + str(test_ten()) + " \n")
    results.append("30%: " + str(test_thirty()) + " \n")
    results.append("60% " + str(test_sixty()) + " \n")
    results.append("100%: " + str(test_full()) + " \n")
    for i in range(3):
        results.append("trial " + str(i) + " k = 5, r = 2km: " + str(hubs_test(5, 2)) + " \n")
    for i in range(3):
        results.append("trial " + str(i) + " k = 10, r = 2km: " + str(hubs_test(10, 2)) + " \n")
    for i in range(3): 
        results.append("trial " + str(i) + " k = 20, r = 2km: " + str(hubs_test(20, 2)) + " \n")
    for i in range(3):
        results.append("trial " + str(i) + " k = 40, r = 2km: " + str(hubs_test(40, 2)) + " \n")
    file1.writelines(results)
    file1.close()
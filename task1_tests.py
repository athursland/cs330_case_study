"""
Runtime tests for our team's implementation of the algorithms described in task1
"""

import task1
import time

### globals
global data
global interval

### datasets
datasets = ['geolife-cars-ten-percent.csv', 'geolife-cars-thirty-percent.csv', 'geolife-cars-sixty-percent.csv', 'geolife-cars.csv']

def task1_test(k, r, fname):
    """
    input: integer k 
    """
    task1.data = []
    start = time.time()
    task1.main(k, r, fname)
    end = time.time()
    return (end-start)*1000 # milliseconds

if __name__=="__main__":
    results = []
    name = ['10%', '30%', '60%', '100%']
    k_values = [5, 10, 20, 40]
    
    file1 = open('task1_tests.txt', 'w')
    
    for i in range(4):
        results.append("Trial 1,  k = {}, r = 2km: {} \n".format(k_values[i], task1_test(k_values[i], 2, datasets[0])))
        results.append("Trial 2,  k = {}, r = 2km: {} \n".format(k_values[i], task1_test(k_values[i], 2, datasets[0])))
        results.append("Trial 3,  k = {}, r = 2km: {} \n\n".format(k_values[i], task1_test(k_values[i], 2, datasets[0])))

    for i in range(4):
        results.append("{} results: {} \n".format(name[i], task1_test(10, 8, datasets[i])))
    
    file1.writelines(results)
    file1.close()
    print(results)

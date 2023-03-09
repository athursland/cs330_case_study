"""
tests for task1
"""

import task1

### globals
global data
global interval

def test_ten():
    data = []
    task1.import_data('geolife-cars-ten-percent.csv')
    task1.preprocess(data) # step 2
    print("points in dataset: ", len(data))
    print("10% time: ", interval)

if __name__=="__main__":
    test_ten()
"""
experiments for task 2
"""

import task2
import time

filename = 'geolife-cars-ten-percent.csv'
trajectories = ['128-20080503104400', '010-20081016113953', '115-20080520225850', '115-20080615225707']

def main(T):
    """
    input: original input trajectory T 
    """
    T_star = task2.simplify_trajectory(T, 0.03)
    return (len(T)/len(T_star))

if __name__ == "__main__":
    task2.import_data(filename)
    results = []
    file2 = open('task2_tests.txt', 'w')
    for i in range(4):
        T = [x[1:] for x in task2.data if x[0] == trajectories[i]]
        results.append("Compression ratio for id = {} : {} \n".format(trajectories[i], main(T)))
    file2.writelines(results)
    file2.close()
    print(results)



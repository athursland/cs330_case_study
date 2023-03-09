"""
experiments for task 3 
ali noa mike
"""
from matplotlib import pyplot as plt
import task3

filename = 'geolife-cars-sixty-percent.csv'
trajectory_pairs = [('128-20080503104400', '128-20080509135846'), 
('010-20081016113953', '010-20080923124453'), ('115-20080520225850', '115-20080615225707')]

if __name__ == "__main__":
    task3.import_data(filename)
    results = []
    #file3 = open('task3_tests.txt', 'w')
    for i in range(3):
        T1 = [x[1:] for x in task3.data if x[0] == trajectory_pairs[i][0]]
        T2 = [x[1:] for x in task3.data if x[0] == trajectory_pairs[i][1]]
        results.append(task3.main(T1, T2))

    plt.hist(results[0][0])
    plt.show()
    #file3.writelines(results)
    #file3.close()
    print(results)

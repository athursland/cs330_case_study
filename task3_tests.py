"""
experiments for task 3 
ali noa mike
"""
from matplotlib import pyplot as plt
import task3

filename = 'geolife-cars.csv'
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

    # first trajectory pair
    for i in range(3):
        fig, (ax1, ax2) = plt.subplots(1, 2)
        plt.suptitle('Lengths of edges in Eavg and Emax for trajectory pair {}'.format(i))
        ax1.hist(results[i][0]) # Eavg
        ax1.set_title('Eavg')
        ax2.hist(results[i][1]) #Emax
        ax2.set_title('Emax')
        plt.savefig('task3_figure_{}'.format(i))
    
    # second trajectory pair
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.hist(results[0][0]) # Eavg
    ax2.hist(results[0][1]) #Emax
    plt.show()
    #file3.writelines(results)
    #file3.close()
    print(results)

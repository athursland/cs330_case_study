"""
experiments for task 3 
ali noa mike
"""
from matplotlib import pyplot as plt
import task2
import task3

filename = 'geolife-cars.csv'
trajectory_pairs = [('128-20080503104400', '128-20080509135846'), 
('010-20081016113953', '010-20080923124453'), ('115-20080520225850', '115-20080615225707')]

def histogram_pairs():
    # first experiment: plotting trajectory pairs
    results = []
    for i in range(3):
        T1 = [x[1:] for x in task3.data if x[0] == trajectory_pairs[i][0]]
        T2 = [x[1:] for x in task3.data if x[0] == trajectory_pairs[i][1]]
        results.append(task3.main(T1, T2))

    for i in range(3):
        fig, (ax1, ax2) = plt.subplots(1, 2)
        plt.suptitle('Lengths of edges in Eavg and Emax for trajectory pair {}'.format(trajectory_pairs[i]))
        ax1.hist(results[i][0]) # Eavg
        ax1.set_title('Eavg')
        ax1.set_xlabel('Edge length')
        ax1.set_ylabel('Counts')
        ax2.hist(results[i][1]) #Emax
        ax2.set_title('Emax')
        ax2.set_xlabel('Edge length')
        ax2.set_ylabel('Counts')
        plt.savefig('task3_pairs_figure_{}'.format(i), bbox_inches='tight')
    return

def simplified_eavg():
    # second experiment: simplification under different epsilons
    eps = [0.03, 0.1, 0.3]
    trajectories = ['115-20080520225850', '115-20080615225707']
    T3 = [x[1:]  for x in task3.data if x[0] == trajectories[0]]
    T4 = [x[1:]  for x in task3.data if x[0] == trajectories[1]]
    
    plots = []
    plt.clf()
    for i in range(3):
        T3_star = task2.simplify_trajectory(T3, eps[i])
        T4_star = task2.simplify_trajectory(T4, eps[i])
        T3_T4_eavg = task3.dtw(T3_star, T4_star)
        #plots.append(T3_T4_eavg)
        plt.hist(T3_T4_eavg, alpha = 0.5, label="ε = {}".format(eps[i]))
    plt.xlabel('Edge lengths')
    plt.ylabel('Counts')
    plt.title('Eavg of T ε1 and T ε2 for ε = [0.03, 0.1, 0.3]')
    plt.legend()
    plt.savefig('task3_eavg_figure')

if __name__ == "__main__":
    task3.import_data(filename)
    histogram_pairs()
    simplified_eavg()
    

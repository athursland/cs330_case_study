"""
Visualizations for Task 1
"""

import task1
from matplotlib import pyplot as plt

def visualize(hubs, data):
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    plt.scatter(x, y, s = 5, alpha = 0.05)

    x_hubs = [center[1][0] for center in hubs]
    y_hubs = [center[1][1] for center in hubs]
    plt.scatter(x_hubs, y_hubs, color = 'r')

    plt.xlabel("X-coords")
    plt.ylabel("Calorie Burnage")
    plt.show()
    return
    
if __name__ == "__main__":
    r = 8
    task1.import_data(task1.full_dataset) # step 1
    task1.preprocess(task1.data) # step 2
    hubs = task1.hubs(10)
    visualize(hubs, task1.data)
import math
from typing import List, Tuple
import csv
from matplotlib import pyplot as plt

filename = 'geolife-cars.csv'
data = []

def import_data(fname):
    """
    import data from csv
    """
    global data
    with open(fname, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None) # skip the headers
        for row in reader:
            id = row[1]
            x = float(row[2])
            y = float(row[3])
            data.append((id, x, y))

def dist(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def dotProduct(A,B):
    return A[0]*B[0]+A[1]*B[1]

def dist_point_segment(q: Tuple[float, float], e): #d in the case study doc
    # Compute the squared length of the segment e
    a = e[0]
    b = e[1]
    l2 = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
    #return distance to closest of the endpoints
    if l2 == 0:
        return min(dist(q, a), dist(q,b))

    AB = [e[1][0]-e[0][0],e[1][1]-e[0][1]]
    AQ = [q[0]-e[0][0],q[1]-e[0][1]]
    BQ = [q[0]-e[1][0],q[1]-e[1][1]]
    if dotProduct(AB,AQ)==0 or dotProduct(AB,BQ)==0:
        return (abs(((b[0] - a[0])* (a[1]-q[1])) - ((a[0] - q[0]) * (b[1]-a[1])))/ math.sqrt(l2))
    else:
        return min(dist((e[0][0],e[0][1]),q),dist((e[1][0],e[1][1]),q))


#function that returns the 2 points closest to p from list of points
def closest_points(p, points):
    closest, second_closest = None, None
    min_dist, sec_min_dist = math.inf, math.inf
    for point in points:
        if dist(p, point) < min_dist:
            second_closest = closest
            sec_min_dist = min_dist
            closest = point
            min_dist = dist(p, point)
        elif dist(p, point) < sec_min_dist:
            second_closest = point
            sec_min_dist = dist(p, point)

    return closest, second_closest

def simplify_trajectory(T: List[Tuple[float, float]], eps: float) -> List[Tuple[float, float]]:
    if len(T) < 3:
       # Base case: return the input trajectory if it has 2 or fewer points
       return []

    T_start=T[0]
    T_end=T[-1]

    max_dist, max_idx = max((dist_point_segment(T[i], (T_start, T_end)), i) for i in range(1, len(T) - 1))
    
    if max_dist>eps:
       simplified_left= simplify_trajectory(T[:max_idx+1],eps)
       simplified_right= simplify_trajectory(T[max_idx:],eps)
       return simplified_left[:-1] + simplified_right
       #simplify_trajectory(T[maxDpoint:],eps)
    else:
       return [T[0],T[-1]]
    '''
    if max_dist<=eps:
        return [T[0],T[-1]]
    else:
        simplified_left= simplify_trajectory(T[:max_idx+1],eps)
        simplified_right= simplify_trajectory(T[max_idx:],eps)
        return simplified_left[:-1] + simplified_right
    '''



def visualize(t, ts1, ts2, ts3):
    """
    create line plot for visualizing output
    """
    T_star_1_x = [point[0] for point in ts1]
    T_star_1_y = [point[1] for point in ts1]
    T_star_2_x = [point[0] for point in ts2]
    T_star_2_y = [point[1] for point in ts2]
    T_star_3_x = [point[0] for point in ts3]
    T_star_3_y = [point[1] for point in ts3]

    T_x = [point[0] for point in t]
    T_y = [point[1] for point in t]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.suptitle('Trajectory simplifications on id = 128-20080503104400 for eps = 0.03, 0.1, 0.3')
    ax1.set_title('eps = 0.03')
    ax1.plot(T_x, T_y, color = 'blue', label = 't')
    ax1.plot(T_star_1_x, T_star_1_y, color = 'red', linewidth = 0.7, marker = '.', markersize=5, label = 't*')
    ax1.legend()
    ax2.set_title('eps = 0.1')
    ax2.plot(T_x, T_y, color = 'blue', label = 't')
    ax2.plot(T_star_2_x, T_star_2_y, color = 'red', linewidth = 0.7, marker = '.',  markersize=5, label = 't*')
    ax2.legend()
    ax3.set_title('eps = 0.3')
    ax3.plot(T_x, T_y, color = 'blue', label = 't')
    ax3.plot(T_star_3_x, T_star_3_y, color = 'red', linewidth = 0.7, marker = '.',  markersize=5, label = 't*')
    ax3.legend()
    plt.show()

    plt.legend()
    plt.xlabel('x-coordinates')
    plt.ylabel('y-coordinates')
    return

if __name__ == '__main__':
    ### visualize for eps = 0.03 
    import_data(filename)
    T = [x[1:]  for x in data if x[0] == "128-20080503104400"]
    T_star_1 = simplify_trajectory(T, 0.03)
    T_star_2 = simplify_trajectory(T, 0.1)
    T_star_3 = simplify_trajectory(T, 0.3)
    visualize(T, T_star_1, T_star_2, T_star_3)
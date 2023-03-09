import math
import heapq
from typing import List, Tuple
import csv
from matplotlib import pyplot as plt


filename = 'geolife-cars-ten-percent.csv'
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
        return ((((b[0] - a[0])* (a[1]-q[1])) - ((a[0] - q[0]) * (b[1]-a[1])))/ math.sqrt(l2))
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
    simplified = [T[0],T[-1]]
    maxD = 0
    maxDpoint = None
    #pq = []
    for i in range(1,len(T)-1):
        two_closest = closest_points(T[i], simplified)
        d = dist_point_segment(T[i], (two_closest[0], two_closest[1]))
        #print(simplified)
        if maxD>d:
            maxD = d
            maxDpoint = T[i]
    T.remove(maxDpoint)
    simplified.append(maxDpoint)

    if maxD<eps:
        return simplified
    else:
        simplify_trajectory(T[0:maxDpoint],eps)
        simplify_trajectory(T[maxDpoint:],eps)






if __name__ == '__main__':


    import_data(filename)
    T = [x[1:]  for x in data if x[0] == "128-20080503104400"]
    print(len(T))
    print(simplify_trajectory(T, 0.03))
import math
import heapq
from typing import List, Tuple
import csv

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
   """Compute the Euclidean distance between two points."""
   x1, y1 = p1
   x2, y2 = p2
   return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def dotProduct(A,B):
   return A[0]*B[0]+A[1]*B[1]

def dist_point_segment(q: Tuple[float, float], e): #d
   """Compute the distance between a point q and a segment e."""
   # Compute the squared length of the segment e
   a = e[0]
   b = e[1]
   l2 = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
   '''
  
   # If the segment has zero length, return the distance to its endpoints
   if l2 == 0:
       return math.sqrt((q[0] - e[0][0]) ** 2 + (q[1] - e[0][1]) ** 2), e[0]

   # Compute the parameter t of the closest point p on the segment e to q
   t = max(0, min(1, ((q[0] - e[0][0]) * (e[1][0] - e[0][0]) + (q[1] - e[0][1]) * (e[1][1] - e[0][1])) / l2))

   # Compute the closest point p on the segment e to q
   p = (e[0][0] + t * (e[1][0] - e[0][0]), e[0][1] + t * (e[1][1] - e[0][1]))

   # Compute the distance between q and p
   dist = math.sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)

   return dist, p
  
  
  
   '''
   AB = [e[1][0]-e[0][0],e[1][1]-e[0][1]]
   AQ = [q[0]-e[0][0],q[1]-e[0][1]]
   BQ = [q[0]-e[1][0],q[1]-e[1][1]]
   if dotProduct(AB,AQ)==0 or dotProduct(AB,BQ)==0:
       return ((((b[0] - a[0])* (a[1]-q[1])) - ((a[0] - q[0]) * (b[1]-a[1])))/ math.sqrt(l2))
   else:
       return min(dist((e[0][0],e[0][1]),q),dist((e[1][0],e[1][1]),q))


def simplify_trajectory(T: List[Tuple[float, float]], eps: float) -> List[Tuple[float, float]]:
   """Simplify a trajectory using the TS-greedy algorithm with a priority queue."""
   # Start with the first point in the trajectory
   simplified = [T[0], T[-1]]

   # Initialize the priority queue with the distances from each point to the first point
   pq = []
   for i in range(1, len(T) -1):
       d = dist_point_segment(T[i], (simplified[-1], simplified[-2]))
       heapq.heappush(pq, (-d, i))
      # heapq.heappush(pq, (-dist(T[i], T[0]), i))


   print(len(pq))
   # Process each point in the priority queue
   while len(pq) > 1:
       _, i = heapq.heappop(pq)
       p = T[i]
       print(len(pq))

       # Compute the distance between the point and the simplified trajectory
       d = dist_point_segment(p, (simplified[-1], simplified[-2]))
       #calculate the distance from current point to the segment made by the
       # two points closest to the current point already in the trajectory


       # If the distance is greater than eps, add the point to the simplified trajectory
       if d > eps:
           simplified.append(p)

           # Update the priority queue with the distances from the new point to each remaining point
           for j in range(i+1, len(T)):
               heapq.heapreplace(pq, (-dist(T[j], p), j))


   print(len(simplified))
   return simplified






if __name__ == '__main__':

   import_data(filename)
   T = [x[1:]  for x in data if x[0] == "128-20080503104400"]
   print(len(T))
   print(simplify_trajectory(T, 0.3))

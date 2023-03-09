"""
task3 
noa mike ali dylan
"""

import math

def dtw(seriesA, seriesB):
  
   A = seriesA
   B = seriesB
   n = len(seriesA)
   m = len(seriesB) 

   if n < m:
       A, B = B, A

   #base cases, fill first and if any series is 1 element
   DP = [[None for _ in range(m)] for _ in range(n)]
   DP[0][0] = dist(A[0], B[0])
   for j in range(1, m):
       DP[0][j] = DP[0][j - 1] + dist(A[0], B[j])

   for i in range(1, n):
       DP[i][0] = DP[i - 1][0] + dist(A[i], B[0])

   for i in range(1, n):
       for j in range(1, m):
           DP[i][j] = dist(A[i], B[j]) + min(DP[i][j - 1], DP[i - 1][j], DP[i - 1][j - 1])

   def find_min(n, m):
       min = (0, m)
       for i in range(1, n):
           if DP[i][m] < DP[min[0]][min[1]]:
               min = (i, m)
       return min #function to find the minimum distance b/w points

   distances = []

   for k in range(0, m):
       pair = find_min(n, k)
       distances.append(dist(A[pair[0]], B[pair[1]]))

   return DP[n - 1][m - 1]

#Frechet Distance Function
def fd(seriesA, seriesB):
   A = seriesA
   B = seriesB
   n = len(seriesA)
   m = len(seriesB)

   if n < m:
       A, B = B, A

   DP = [[None for _ in range(m)] for _ in range (n)]
   DP[0][0] = dist(A[0], B[0])
   for j in range(1, m):
       DP[0][j] = DP[0][j-1] + dist(A[0], B[j])

   for i in range(1, n):
       DP[i][0] = DP[i-1][0] + dist(A[i], B[0])

   for i in range(1, n):
       for j in range(1, m):
           DP[i][j] = max(dist(A[i], B[j]),min(DP[i][j-1], DP[i-1][j], DP[i-1][
               j-1]))

   def find_min(n,m):
       min = (0,m)
       for i in range(1,n):
           if DP[i][m] < DP[min[0]][min[1]]:
               min = (i, m)
       return min

   distances = []

   for k in range(0,m):
       pair = find_min(n,k)
       distances.append(dist(A[pair[0]],B[pair[1]]))

   print(distances)

   return DP[n-1][m-1]

#Distance Formula
def dist(a, b):
  return math.dist([a[0], a[1]], [b[0], b[1]])

def main():
   A = [(0, 0), (1,1), (2,2)]
   B = [(0, 1), (2,1)]
   print(dtw(A, B))
   print(fd(A, B))

if __name__ == '__main__':
   main()
"""
task3 
noa mike ali dylan
"""

import math

#import matplotlib.pyplot as plt

#Dynamic Time Warping Function
def dtw(seriesA, seriesB):


  # Swap seriesA and seriesB if seriesA is shorter

  if len(seriesA) < len(seriesB):
      seriesA, seriesB = seriesB, seriesA


  #init first 2 rows of matrix w/ infinity


  prev_row = [float('inf') for j in range(len(seriesB) + 1)]

  curr_row = [float('inf') for j in range(len(seriesB) + 1)]

  #top left = 0
  curr_row[0] = 0


  #first row = distance
  for j in range(1, len(curr_row)):

      curr_row[j] = curr_row[j - 1] + dist(seriesA[0], seriesB[j - 1])

  # optimal decision = min(distance + up left, up, left)
  for i in range(1, len(seriesA) + 1):
      prev_row, curr_row = curr_row, prev_row

      curr_row[0] = prev_row[0] + dist(seriesA[i - 1], seriesB[0])


      for j in range(1, len(seriesB) + 1):


          d = dist(seriesA[i - 1], seriesB[j - 1])


          curr_row[j] = min(prev_row[j - 1] + d, prev_row[j] + d,


                            curr_row[j - 1] + d)


  #return last cell
  return curr_row[-1]



#Frechet Distance Function
def fd(seriesA, seriesB):
   A = seriesA
   B = seriesB
   n = len(seriesA)
   m = len(seriesB)

   A = seriesA
   B = seriesB
   n = len(seriesA)
   m = len(seriesB)     #A < B

   if n>m:
       n = len(seriesB)
       m = len(seriesA)
       A = seriesB
       B = seriesA

   T = [[None for _ in range(m)] for _ in range (n)]
   T[0][0] = dist(A[0], B[0])
   for j in range(1, m):
       T[0][j] = T[0][j-1] + dist(A[0], B[j])

   for i in range(1, n):
       T[i][0] = T[i-1][0] + dist(A[i], B[0])

   for i in range(1, n):
       for j in range(1, m):
           T[i][j] = max(dist(A[i], B[j]),min(T[i][j-1], T[i-1][j], T[i-1][j-1]))

   def find_min(n,m):
       min = (0,m)
       for i in range(1,n):
           if T[i][m] < T[min[0]][min[1]]:
               min = (i, m)
       return min

   distances = []

   for k in range(0,m):
       pair = find_min(n,k)
       distances.append(dist(A[pair[0]],B[pair[1]]))

   dict = count_elements(distances)
   plot_histogram(dict)
   print(distances)

   return T[n-1][m-1]



#Distance Formula
def dist(a, b):
  return math.dist([a[0], a[1]], [b[0], b[1]])



#Creates Frequency Dictionary for Histogram
def count_elements(seq):
   hist = {}
   for i in seq:
       hist[i] = hist.get(i,0) + 1
   return hist

#Plots Histogram
def plot_histogram(dict):
   ind = []
   freq = []
   for key in dict:
       ind.append(key)
       freq.append(dict.get(key))
  # plt.bar(ind, freq)
   #plt.show()

def main():
   A = [(0, 0), (1,1), (2,2)]
   B = [(0, 1), (2,1)]
   print(dtw(A, B))

if __name__ == '__main__':
   main()


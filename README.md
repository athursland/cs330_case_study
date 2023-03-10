# CompSci 330 Case Study README

## Authors
 - Ali Thursland - akt21
 - Mike Kim - bk146
 - Noa Nir - nn83
 - Dylan Schneiderman - mds98

## Zip Contents

Our ZIP file contains our source code in and a PDF of our powerpoint presentation for Case Study Part 1. All of our solutions are implemented using Python. Our source code contains the following .py files: 

- task1.py - contains our implementation of the preprocessing procedure, density, hubs, and all requisite helper functions. Also contains the code needed to reproduce our visualizatiosn for Task 1. 
- task1_tests.py - contains tests we used to produce experimental outputs described in Task 1.
- task2.py - contains our implementation of simplified_trajectory and all requisite helper functions.
- task2_tests.py - contains the tests we used to produce experimental outputs described in Task 2.
- task3.py - contains our implementation of the monotone assignments described in Task 3.
- task3_tests.py - contains the code needed to produce the histograms necessary for interpreting the performance of our Task 3 algorithms.

NOTE: We did not include the 'geolife-cars.csv' family of datasets in our ZIP file. These must be in the same directory path as the source code files for the data to import correctly. Please take note of this when attempting to reproduce our results.

The ZIP file also contains the following .txt files:
- task1_tests.txt - This text file contains the non-figure results of our case study. First, it contains our algorithm's runtime in ms for k=5,10,20,40 and r =2km. Then, under that, this file has our algorithm's runtime using k=10, r=8km, on the full dataset, and the 10%, 30%, and 60% subsets.
- task2_tests.txt - This file has the compression ratios |T |/|T′| for trajectories 128-20080503104400, 010-20081016113953, 115-20080520225850, and 115-20080615225707 using our implementation of TS-greedy for ε = 0.03km.

The figures folder contains the visualizations described in the assignment:
  - Figure_1.png - Scatter plot for task 1, representing the set of hubs identified using k = 10 and r = 8km and points of P in the background of the same figure using different markers and colors.
  - Figure_2.png - Line plot for task 2, depicting the trajectory with id = 128-20080503104400 and its simplification using the algorithm implemented in task 2 for ε = 0.03km,0.1km, and 0.3km. The original trajectory is colored blue while the simplified trajectory is colored red.
  - task3_eavg_figure.png - Histogram for task 3, representing a the Eavg monotone assignment between the simplifications of T1 = 115-20080520225850 and T2 = 115-20080615225707 for ε = 0.03km, 0.1km, 0.3km.
  - task3_pairs_figure_0.png - Histogram for task 3, representing the lengths of edges in Eavg and Emax for the trajectory pair with IDs(128-20080503104400, 128-20080509135846)
  - task3_pairs_figure_1.png - Histogram for task 3, representing the lengths of edges in Eavg and Emax for the trajectory pair with IDs (010-20081016113953, 010-20080923124453)
  - task3_pairs_figure_2.png - Histogram for task 3, representing the lengths of edges in Eavg and Emax for the trajectory pair with IDs (115-20080520225850, 115-20080615225707)

To reproduce our experimental results for each task, run task1_tests.py, task2_tests.py, then task3_tests.py. task1_tests.py and task2_tests.py write the resutls of our experiments to the corresponding text files, while task3_tests.py creates and saves the visualizations for Task 3. In addition, to reproduce our visualizations for Task 1 and Task 2, run task1_viz.py and then task2.py.

 ## External Dependencies

The only external library we used is matplotlib, which we utilize for creating our visualizations. Run the following command to install matplotlib:

    pip3 install matplotlib
    
matplotlib is necessary to run task1.py, task2.py,and  task3_tests.py. All of the other source code files can be run without any external dependencies.


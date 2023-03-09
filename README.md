# CompSci 330 Case Study README

## Authors
 - Ali Thursland - akt21
 - Mike Kim - bk146
 - Noa Nir - nn83
 - Dylan Schneiderman - mds98

## Zip Contents
Our zip file contains 4 csv files that were provided to us as part of the case study. 

 - geolife-cars.csv
 - geolife-cars-ten-percent.csv
 - geolife-cars-thirty-percent.csv
 - geolife-cars-sixty-percent.csv

It also contains the following python files:

- task1.py - this is the python file that contains the coded algorithms asked of us in task1.
- task1_viz.py - this is what you can run to see our visualizations made from the dataset provided.
- task1_tests.py - this file contains the tests that we are asked to run.
- task2.py - this is the python file that contains the coded algorithms asked of us in task2.
- task2_tests.py - this file contains the tests that we are asked to run for task 2.
- task3.py - this is the python file that contains the coded algorithms asked of us in task3.
- task3_tests.py - this file contains the tests that we are asked to run for task 3.

There are also some text files:
- task1_tests.txt - This text file contains the non-figure results of our case study. First, it contains our algorithm's runtime in ms for k=5,10,20,40 and r =2km. Then, under that, this file has our algorithm's runtime using k=10, r=8km, on the full dataset, and the 10%, 30%, and 60% subsets.
- task2_tests.txt - This file has the compression ratios |T |/|T ′| for trajectories 128-20080503104400, 010-20081016113953, 115-20080520225850, and 115-20080615225707 using TS-greedy for ε = 0.03km.

Finally, it contains a Figures folder, which contains the images in our report.
- Figures
  - Figure_1.png - this is a scatter plot of the set of hubs identified using k = 10 and r = 8km and points of P in the background of the same figure using different markers and colors.
  - Figure_2.png - this is a plot of the trajectory ID 128-20080503104400 and its simplification using the task-2 function for ε = 0.03,0.1,0.3 (kilometers). Each figure contains two line plots: trajectory and its simplification, with markers of different colors
  - task3_eavg_figure.png - a simplification of T1 = 115-20080520225850, T2 = 115-20080615225707 for ε = 0.03,0.1,0.3 (kilometers).
  - task3_pairs_figure_0.png - a histogram of lengths of edges in Eavg and Emax for trajectories (128-20080503104400, 128-20080509135846)
  - task3_pairs_figure_1.png - a histogram of lengths of edges in Eavg and Emax for trajectories (010-20081016113953, 010-20080923124453)
  - task3_pairs_figure_2.png - a histogram of lengths of edges in Eavg and Emax for trajectories (115-20080520225850, 115-20080615225707)

To reproduce our results, run task1_viz.py, task1_tests.py, then task2_tests.py, then task3_tests.py

 ## External Dependencies

The only external library we used is matplotlib. Make sure matplotlib is installed, or our code won't work. Install matplotlib by tying the following command in your terminal: 

    pip3 install matplotlib


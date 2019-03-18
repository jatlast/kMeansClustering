########################################################################
# CSC 546
#   Homework 6
#   Clustering – (Everyone)
#       a.  Write the code to perform the k-means clustering on 1-dimensional data. Use
#           the data provided in HW_6_data.dat located on BB. Run your code for 2 and
#           3 clusters and plot out the data on a line and highlight the means of the two
#           clusters as they move.
#       b.  (in addition Graduate Students do this) Extend your code to perform the kmeans
#           clustering on 2-dimensional data. Use the data provided in
#           HW_6_data_2D.dat located on BB. Run your code for 2 and 3 clusters and
#           plot out the data as a 2-dimensional scatterplot and plot the corresponding
#           cluster centers.
#
# Note: this code is available on GitHub 
#   https://github.com/jatlast/kMeansClustering.git
#
# The following websites were referenced:
#   For Python scatterplot tools
#   https://pythonspot.com/matplotlib-scatterplot/
#
########################################################################

# required for picking initial mean poin(s) from supplied data set
import random
# required for sqrt function in Euclidean Distance calculation
import math
# required for scatterplot visualization
import numpy as np
import matplotlib.pyplot as plt
# required for determining data file contents on the fly
import re

# allow command line options
import argparse
parser = argparse.ArgumentParser(description="perform the k-means clustering on 1 to 2-dimensional data")
parser.add_argument("-f", "--filename", default="./data/HW_6_data_1D.dat", help="file name (and path if not in . dir)")
parser.add_argument("-c", "--clusters", type=int, choices=[2, 3], default=2, help="number of clusters to try")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")
args = parser.parse_args()

# create a dictionary of list objects equal to the number of clusters to test
clust_dict = {}
for i in range(1, args.clusters + 1):
    clust_dict[i] = []

if args.verbosity == 2:
    print(f"filename={args.filename} : clusters={args.clusters} : len(clust_dict)={len(clust_dict)}")
elif args.verbosity == 1:
    print(f"{args.filename} : {args.clusters} : {len(clust_dict)}")

# compute Euclidean distance between any two given vectors with any length.
# Note: adapted from CSC 587 Adv Data Mining, HW02
# Note: a return value < 0 = Error
def EuclideanDistanceBetweenTwoVectors(vOne, vTwo):
    distance = 0
    v_one_len = len(vOne)
    v_two_len = len(vTwo)
    # vOne & vTwo must be of equal length
    if(v_one_len != v_two_len):
        return -1

    for p in range(0, v_one_len):
        distance += math.pow((abs(vOne[p] - vTwo[p])), 2)
    return math.sqrt(distance)

def OneDimensionalDistanceBetweenTwoPoints(One, Two):
    distance = 0
    return abs(One - Two)

# 1D scatterplots
def Scatterplot1D(x):
    val = 0 # where the data will appear on the y-axis
#    plt.plot(50, np.zeros_like(50) + val, 'ro')
    plt.plot(x, np.zeros_like(x) + val, 'g*')
    plt.title('1D Scatter Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# 2D scatterplots
def Scatterplot2D(x, y=0):
    # Create data
    colors = (0,0,0)
    area = np.pi*3
    
    # Plot
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.title('2D Scatter Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# read in the 1-dimensional data file
with open(args.filename, mode='r') as data_file:
    x = []
    y = []
    # parse data file
    for line in data_file:
        match = re.search(r'(\d+\.\d+)\s*(\d+\.\d+)?', line)
        if match:
            if match.group(1):
                x.append(float(match.group(1)))
            if match.group(2):
                y.append(float(match.group(2)))
        else:
            print(f"Warning: no match for line ({line})")
    x_len = len(x)
    y_len = len(y)
    mean_dict = {}
    for j in range(1, args.clusters + 1):
        rand_int = random.randint(1,x_len)
        if y_len > 0:
            mean_dict[j] = (x[rand_int], y[rand_int])
        else:
            mean_dict[j] = x[rand_int]
    
    for i in range(0, x_len):
        min_distance = 10000
        min_index = 0
        for j in range(1, args.clusters + 1):
            if y_len > 0:
                vec_two = (x[i], y[i])
                EuclideanDistance = EuclideanDistanceBetweenTwoVectors(mean_dict[j], vec_two)
                if EuclideanDistance < min_distance:
                    min_distance = EuclideanDistance
                    min_index = j
            else:
                distance_1D = abs(mean_dict[j] - x[i])
                if distance_1D < min_distance:
                    min_distance = distance_1D
                    min_index = j
        if y_len > 0:
            clust_dict[min_index].append(vec_two)
        else:
            clust_dict[min_index].append(x[i])

    print(f"x_len({x_len}):y_len({y_len})")
    print(f"mean_dict({mean_dict})")
#    print(f"clust_dict({clust_dict})")
    for i in range(1, args.clusters + 1):
        print(f"clust len({len(clust_dict[i])}) mean({np.mean(clust_dict[i])})")

    # if y_len > 0:
    #     Scatterplot2D(x, y)
    # else:
    #     Scatterplot1D(x)
    # print(f"{rand_int} : {i} : {x_len}")

    # vec_one = (x[rand_int], y[rand_int])
    # vec_two = (x[0], y[0])

    # EuclideanDistance = EuclideanDistanceBetweenTwoVectors(vec_one, vec_two)
    # print(f"Euclidean distance = {EuclideanDistance}")


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
parser.add_argument("-f", "--filename", default="./data/HW_6_data_file.dat", help="file name (and path if not in . dir)")
parser.add_argument("-c", "--clusters", type=int, choices=[2, 3], default=2, help="number of clusters to try")
#parser.add_argument("x", type=int, help="the base")
#parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")
args = parser.parse_args()

if args.verbosity == 2:
    print(f"filename={args.filename} : clusters={args.clusters}")
elif args.verbosity == 1:
    print(f"{args.filename} : {args.clusters}")
else:
    print("v = 0")

# compute Euclidean distance between any two given vectors with any length.
# Note: adapted from CSC 587 Adv Data Mining, HW02
def EuclideanDistanceBetweenTwoPoints(One, Two):
    distance = 0
    distance += math.pow((abs(One - Two)), 2)
    return math.sqrt(distance)

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

# create a dictionary of list objects equal to the number of clusters to test
clust_dict = {}
for i in range(1, args.clusters + 1):
    clust_dict[i] = []

print(f"clust_dict({len(clust_dict)})")

# read in the 1-dimensional data file
with open(args.filename, mode='r') as data_file:
#    line_one = data_file.readline()
    # dimensionality = 0
    # d1 = re.compile(r'(\d+\.\d+)')
    # d2 = re.compile(r'(\d+\.\d+)\s+(\d+\.\d+)')

    # if d2.match(line_one):
    #     dimensionality = 2
    # elif d1.match(line_one):
    #     dimensionality = 1
    # else:
    #     print("Error: unknown file dimensionality")
    #     exit -1

    # match = re.search(r'(\d+\.\d+)\s+(\d+\.\d+)?', line)
    # if match:
    #     print(match.group())
    #     print(match.group(1))
    #     print(match.group(2))

    i = 0
    x = []
    y = []
    # parse data file
    for line in data_file:
        match = re.search(r'(\d+\.\d+)\s+(\d+\.\d+)?', line)
        if match:
            if match.group(1):
                x.append(float(match.group(1)))
            if match.group(2):
                y.append(float(match.group(2)))

    rand_int = random.randint(1,len(x))
    if len(y) > 0:
        Scatterplot2D(x, y)
    else:
        Scatterplot1D(x)

#    Scatterplot1D(x)
#    print(f"{x}")

    print(f"{rand_int} : {i} : {len(x)}")

    EuclideanDistance = EuclideanDistanceBetweenTwoPoints(x[rand_int], x[1])
    print(f"Euclidean distance = {EuclideanDistance}")

# read in the 1-dimensional data file
with open('./data/HW_6_data_2D.dat', mode='r') as data_2D:
#    print(data_2D.readline())
    i = 0
    x = []
    y = []
    # parse data file
    for line in data_2D:
        x.append([])
        y.append([])
        x[i], y[i] = [float(n) for n in line.split('  ')]
        i += 1

    rand_int = random.randint(1,i)
    print(f"{rand_int} : {i} : {len(x)}")
#    Scatterplot2D(x, y)


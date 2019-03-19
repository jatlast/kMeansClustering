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
# required for defaultdict
#from collections import defaultdict

# allow command line options
import argparse
parser = argparse.ArgumentParser(description="perform the k-means clustering on 1 to 2-dimensional data")
parser.add_argument("-f", "--filename", default="./data/HW_6_data_1D.dat", help="file name (and path if not in . dir)")
parser.add_argument("-c", "--clusters", type=int, choices=[2, 3], default=2, help="number of clusters to try")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")
args = parser.parse_args()

# create a dictionary of list objects equal to the number of clusters to test
clust_dict = {}
#clust_dict = defaultdict(list)
for i in range(1, args.clusters + 1):
    clust_dict[i] = []

if args.verbosity > 0:
    print(f"filename={args.filename} : clusters={args.clusters} : len(clust_dict)={len(clust_dict)}")

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

# 1D scatterplot
def Scatterplot1D(dClusters, dMeans, dVariables):
    val = 0 # where the data will appear on the y-axis
    for i in range(1, len(dClusters) + 1):
        plt.plot(dClusters[i], np.zeros_like(dClusters[i]) + val, dVariables['dColors'][i][0])
        plt.plot(dMeans[i], np.zeros_like(dMeans[i]) + val, dVariables['dColors'][i][1])
    plt.title(dVariables['plot_title'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# 2D scatterplot
def Scatterplot2D(dClusters, dMeans, dVariables):
    for i in range(1, len(dClusters) + 1):
        x = []
        y = []
        for j in range(0, len(dClusters[i])):
            x.append(dClusters[i][j][0])
            y.append(dClusters[i][j][1])
        plt.plot(x, y, dVariables['dColors'][i][0])
        plt.plot(dMeans[i][0], dMeans[i][1], dVariables['dColors'][i][1])
    plt.title(dVariables['plot_title'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

variables_dict = {
    'mean_change_max' : 0.9
    , 'mean_change_threshold' : 0.2
    , 'plot_title' : 'Default Title'
    , 'dColors' : {
        1 : ['k.', 'bo'] # blue . data and red o mean
        , 2 : ['g+', 'rP'] # green + data and yellow "filled +" mean
        , 3 : ['cx', 'mX'] # green + data and yellow "filled +" mean
    }
}

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
    
    # loop until the maximum mean change is less than some threshold
    while variables_dict['mean_change_max'] > variables_dict['mean_change_threshold']:
        if args.verbosity > 1:
            print(f"mean_change_max({variables_dict['mean_change_max']}) > {variables_dict['mean_change_threshold']}")
        
        # populate the appropriate number of cluster lists
        for i in range(0, x_len):
            min_distance = 10000    # used to determine the closest mean
            min_index = 0           # stores the index of the closest mean
            # loop over the appropriate number of clusters
            for j in range(1, args.clusters + 1):
                # 2-dimentional
                if y_len > 0:
                    vec_two = (x[i], y[i])
                    EuclideanDistance = EuclideanDistanceBetweenTwoVectors(mean_dict[j], vec_two)
                    if EuclideanDistance < min_distance:
                        min_distance = EuclideanDistance
                        min_index = j
                # 1-dimentional
                else:
                    distance_1D = abs(mean_dict[j] - x[i])
                    if distance_1D < min_distance:
                        min_distance = distance_1D
                        min_index = j

            # 2-dimentional
            if y_len > 0:
                clust_dict[min_index].append(vec_two)
            # 1-dimentional
            else:
                clust_dict[min_index].append(x[i])

        if args.verbosity > 1:
            print(f"x_len({x_len}):y_len({y_len})")
            print(f"mean_dict({mean_dict})")
            for i in range(1, len(clust_dict) + 1):
                print(f"clust len({len(clust_dict[i])}) mean({np.mean(clust_dict[i])})")

        # create the plot graph
        variables_dict['plot_title'] = "Scatter Plot ({:.2f} > {:.2f})".format(variables_dict['mean_change_max'], variables_dict['mean_change_threshold'])
        if y_len > 0:
            Scatterplot2D(clust_dict, mean_dict, variables_dict)
        else:
#            variables_dict['plot_title'] = '1D Scatter Plot (' + str(variables_dict['mean_change_max']) + ' > ' + str(variables_dict['mean_change_threshold']) + ')'
            Scatterplot1D(clust_dict, mean_dict, variables_dict)

        # clear the lists, recalculate the means, and store the maximum change
        for i in range(1, len(clust_dict) + 1):
            # 2-dimentional
            if y_len > 0:
                new_mean = np.mean(clust_dict[i], axis=0) # calculate new mean as 2d array
                # calculate the change in means using Euclidean Distance function
                EuclideanDistance = EuclideanDistanceBetweenTwoVectors(mean_dict[i], new_mean)
                mean_change = EuclideanDistance
            # 1-dimentional
            else:
                new_mean = np.mean(clust_dict[i])           # calculate the new mean value
                mean_change = abs(new_mean - mean_dict[i])  # calculate the change in means
            print(f"new_mean = ({new_mean})")
            print(f"mean_change = ({mean_change})")
            mean_dict[i] = new_mean                     # set recalculated mean
            clust_dict[i] = []                          # clear the list
            # on the first pass set the max to the current
            if i == 1:
                variables_dict['mean_change_max'] = mean_change

            # store the maximum mean change
            if mean_change > variables_dict['mean_change_max']:
                variables_dict['mean_change_max'] = mean_change

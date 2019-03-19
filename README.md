# kMeansClustering

k-means clustering on 1-dimensional &amp; 2-dimensional data.
```
Master's Degree: University of Michigan - Computer Science & Information Systems
Course: CSC 546 - Advanced Artificial Intelligence

Assignment Homework 6: Due: 03/19/2019 5:59 PM
1. Clustering – (Everyone)
    a.  Write the code to perform the k-means clustering on 1-dimensional data. Use
        the data provided in HW_7_data.dat located on BB. Run your code for 2 and
        3 clusters and plot out the data on a line and highlight the means of the two
        clusters as they move.
    b.  (in addition Graduate Students do this) Extend your code to perform the kmeans
        clustering on 2-dimensional data. Use the data provided in HW_6_data_2D.dat
        located on BB. Run your code for 2 and 3 clusters and plot out the data as a 2-dimensional scatterplot and plot the corresponding cluster centers.
```
## False Starts

1) Had difficulty figuring out how to recalculate mean values for 2-dimensional arrays

## Final Solutions

1) Python's numpy library includes a mean function, however, one needs to include the "axis=0" argument to receive a 2-dimensional mean calculation.

## Chosen Technologies

Motivation: Become more familiar with the following.
1) Artificial Intelligence clustering algorithms
2) Python's numpy & matplotlib.pyplot libraries for plot visualizations
3) Developing with Python 3.7 in Windows environment
4) IDE - Visual Studio Code
5) GitHub (I am becoming quite familiar)

## The following websites were referenced

* [Pyplot Tutorial](https://matplotlib.org/users/pyplot_tutorial.html) - For understanding the basics of matplotlib.pyplot
* [Specifying Colors](https://matplotlib.org/users/colors.html) - For pyplot color reference
* [matplotlib.markers](https://matplotlib.org/api/markers_api.html) - For pyplot marker type reference

### Prerequisites

- Python 3.6+

### Installing
```
Just get the "kMeansClustering" project.
It should run in any Python 3.6+ environment
```

### Command Line Specifications
```
> python kMeanClustering.py -h
usage: kMeanClustering.py [-h] [-f FILENAME] [-c {2,3}] [-v {0,1,2}]

perform the k-means clustering on 1 to 2-dimensional data

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        file name (and path if not in . dir)
  -c {2,3}, --clusters {2,3}
                        number of clusters to try
  -v {0,1,2}, --verbosity {0,1,2}
                        increase output verbosity
```

## License

This project is not licensed but feel free to play with any part you so desire.

## Acknowledgments

* matplotlib.org
* Google's vast doorway to every tid-bit of documentation on the internet
* All those wonderfully generous documentation writers and question answerers

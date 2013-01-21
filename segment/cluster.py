#!/usr/bin/python
 
import numpy as np
from scipy.cluster.vq import kmeans2
import colorsys, math

import matplotlib
matplotlib.use('Agg')

import pylab
pylab.close()

def gen_colours(n):
    colors=[]
    for i in np.arange(0., 360., 360. / n):
        hue = i/360.
        lightness = (50 + np.random.rand() * 10)/100.
        saturation = (90 + np.random.rand() * 10)/100.
        colors.append(colorsys.hls_to_rgb(hue, lightness, saturation))
    return colors

def compute_clusters(xy, clusters):
    res, idx = kmeans2(np.array(zip(xy[:,0],xy[:,1])),clusters)
    return res, idx

def gen_random_data():
    # generate 3 sets of normally distributed points around
    # different means with different variances
    pt1 = np.random.normal(1, 0.2, (100,2))
    pt2 = np.random.normal(2, 0.5, (300,2))
    pt3 = np.random.normal(3, 0.3, (100,2))
     
    # slightly move sets 2 and 3 (to make segments seam more obvious visually)
    pt2[:,0] += 1
    pt3[:,0] -= 0.5
     
    xy = np.concatenate((pt1, pt2, pt3))
    return xy

if __name__=="__main__":

    xy = gen_random_data()

    """
    basic scatter ploting (3 clusters)
    """
    pylab.figure()
    res, idx = compute_clusters(xy, 3) # kmeans for 3 clusters
    colours = gen_colours(3)
    coloured_idx = ([colours[i] for i in idx])   # plot colored points

    pylab.scatter(xy[:,0],xy[:,1], c=coloured_idx) # mark centroids as (X)
    pylab.scatter(res[:,0],res[:,1], marker='x', s = 500, linewidths=1)

    pylab.savefig("kmeans_scatter_basic.png")

    """
    multiple scatter plotting
    """
    # produce scatter plots in order to cluster into different groups
    combinations = [2,3,4,5,6,7]

    for c in combinations:
        res, idx = compute_clusters(xy, c)
        colours = gen_colours(c)
        coloured_idx = ([colours[i] for i in idx])

        pylab.figure()
        pylab.scatter(xy[:,0],xy[:,1], c=coloured_idx)
        pylab.scatter(res[:,0],res[:,1], marker='x', s = 500, linewidths=1)
        filename = "kemans_scatter_%s.png" % c
        pylab.savefig(filename)

    """
    subplotting multiples scatters
    """
    # produce a single combined plot for different cluster combinations
    combinations = [1,2,3,4, 5, 6, 7, 8]
    x = len(combinations)
    w = int(math.ceil(math.sqrt(x)))
    h = int(math.ceil(x*1.0/w))

    pylab.figure()
    for n, c in enumerate(combinations):
        colours = gen_colours(c)
        res, idx = compute_clusters(xy, c)
        coloured_idx = ([colours[i] for i in idx])
        sp = pylab.subplot(w,h,n+1)
        sp.scatter(xy[:,0],xy[:,1], c=coloured_idx)
        sp.scatter(res[:,0],res[:,1], marker='x', s = 500, linewidths=1)
        res, idx = compute_clusters(xy, c)

    filename = "kemans_combined.png"
    pylab.savefig(filename)

    #annimating multiple scatters



    #The adjusted rand index could be used to evelulate the how effective the clustering was. 
    #Obviously to do this you need known points. http://scikit-learn.org/dev/modules/clustering.html
    #ARI requires knowledge of the ground truth classes

    #Silhouette Coefficient and others can be used if the ground trough is not understood
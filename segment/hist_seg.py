#!/usr/bin/python
 
import numpy as np
from scipy.cluster.vq import kmeans2
from collections import defaultdict
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

def random_discrete_sample(mu, sigma, n, d):
    pt1 = np.random.normal(mu, sigma, (n,d))
    return  [int(abs(p)) for p in  np.random.normal(mu, sigma, (n,d))]

if __name__=="__main__":

    pt1 = random_discrete_sample(4, 0.9, 800, 1)
    pt2 = random_discrete_sample(30, 10.0, 400, 1)
    pt3 = random_discrete_sample(80, 45.0, 600, 1)
    pt4 = random_discrete_sample(225, 45.0, 200, 1)
    data = np.concatenate((pt1, pt2, pt3, pt4))
    print data

    pylab.figure()
    pylab.hist(data, bins=35)
    pylab.savefig("histogram_basic.png")

    clusters = 4
    res, idx = kmeans2(data,clusters)

    colours = gen_colours(clusters)
    segmented_data = defaultdict(lambda: [])
    for i, group in enumerate(idx):
        segmented_data[colours[group]].append(data[i])

    print segmented_data

    pylab.figure()
    for colour, segment_list in segmented_data.iteritems():
        pylab.hist(segment_list, bins=35, range=(data.min(), data.max()))

    pylab.savefig("histogram_kmenas_segments.png")
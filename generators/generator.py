#!/usr/bin/env python

import math
import random
import numpy as np
from scipy.stats import norm
from scipy.linalg import inv

# generate data for clustering
# we will generate 3 clusters
# cluster 1: number of samples NUM_SAMPLES
NUM_SAMPLES = 42;

# taxpayer age -- normal distribution with mean 35 and variance 5
taxpayerAge = np.round(norm.rvs(
    loc = 35,
    scale = 5,
    size = NUM_SAMPLES
), decimals = 1)

# walkability -- normal distribution with mean 90 and variance of 5
walkability = np.round(norm.rvs(
    loc = 90,
    scale = 5,
    size = NUM_SAMPLES
), decimals = 1)

# distance to park -- normal distribution with mean of 2 and variance of 0.3
distanceToPark = np.round(norm.rvs(
    loc = 2,
    scale = 0.3,
    size = NUM_SAMPLES
), decimals = 1)

# square footage -- normal distribution with mean of 1400 and variance of 500
squareFootage = np.round(norm.rvs(
    loc = 1400,
    scale = 500,
    size = NUM_SAMPLES
))

# lotSize size -- normal distribution with mean of 0.25 and variance of 0.05
lotSize = np.round(norm.rvs(
    loc = 0.25,
    scale = 0.05,
    size = NUM_SAMPLES
), decimals = 2)

# function that naively generates a set with the given size
# using the given source numbers and with approximately the given mean
def generateSamples(source = [], loc = 0, size = NUM_SAMPLES):
    source.sort()
    source = np.array(source)

    samples = np.empty(size)
    samples[0] = random.choice(source)

    i = 1
    while i < size:
        mean = np.mean(samples[:i])
        if mean < loc:
            nextOpts = np.extract(mean < source, source)
        elif loc > mean:
            nextOpts = np.extract(source > mean, source)
        else:
            nextOpts = source
        samples[i] = random.choice(nextOpts)
        i += 1

    random.shuffle(samples)
    return samples

# bedrooms -- integer random {2, 3, 4} average around 3
bedrooms = generateSamples(
    source = [2, 3, 4],
    loc = 3
)

# bathrooms -- float random {1.0, 1.5, 2.0} average around 1.8
bathrooms = generateSamples(
    source = [1, 1.5, 2],
    loc = 1.8
)

# garage -- integer random {0, 1, 2} average around 1.7
garage = generateSamples(
    source = [0, 1, 2],
    loc = 1.7
)

# off street parking -- integer random {0, 1, 2} average around 1.6
parking = generateSamples(
    source = [0, 1, 2],
    loc = 1.6
)

# within walking distance of public schools -- integer {0, 1} average around 0.4
publicSchools = generateSamples(
    source = [0, 1],
    loc = 0.4
)

# within walking distance of private schools -- integer {0, 1} average around 0.2
privateSchools = generateSamples(
    source = [0, 1],
    loc = 0.2
)

# access to highway -- integer {0, 1} average 0.7
highway = generateSamples(
    source = [0, 1],
    loc = 0.4
)

# export as csv file
# human readable headers
header = [
    'Age',
    'Walkability',
    'Distance to Park',
    'Square Footage',
    'Lot Acreage',
    'Bedrooms',
    'Bathrooms',
    'Garage Size',
    'Off-Street Parking',
    'Walkable Public School',
    'Walkable Private School',
    'Highway Access'
]

# ensure all generated data are positive
# transpose data so that each row is a house instead of each column
data = np.absolute(np.transpose([
    taxpayerAge,
    walkability,
    distanceToPark,
    squareFootage,
    lotSize,
    bedrooms,
    bathrooms,
    garage,
    parking,
    publicSchools,
    privateSchools,
    highway
]))

np.savetxt('junk.tsv', data,
    header = '\t'.join(header), # Add column names as comment instead of row
    fmt = '%s',                 # Format all cells as strings
    delimiter = '\t'            # tsv
)

from __future__ import division

def euclidean_distance(list1, list2):
    assert(len(list1) == len(list2)), "The points don't have the same dimension"
    distance = sum([(i - j) ** 2 for i, j in zip(list1, list2)]) ** 0.5
    assert(distance >= 0), "Distance can't be less than 0"
    return distance

def random_ranges(lo, up):
    assert(up >= lo), "Something is wrong"
    from random import random
    return lo + random() * (up - lo)

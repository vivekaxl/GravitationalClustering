from __future__ import division
from Utilities import euclidean_distance
import itertools

class Point:
    newid = itertools.count().next

    def __init__(self, location, velocity=1):
        self.id = Point.newid()
        self.location = location
        self.velocity = velocity
        self.parent = self
        self.rank = -1

    def distance(self, point):
        #  point is of type point
        return euclidean_distance(self.location, point.location)


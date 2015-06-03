from __future__ import division

def makeset(x):
    x.parent = x
    x.rank = 0

def findset(x):
    while x.parent != x:
        x = x.parent
    return x

def union(x, y):
    parent_x = findset(x)
    parent_y = findset(y)
    # In the same set
    if parent_x == parent_y:
        return

    if parent_x.rank > parent_y.rank:
        parent_y.parent = parent_x
    elif parent_y.rank > parent_x.rank:
        parent_x.parent = parent_y
    elif parent_y.parent != parent_x.parent:
        parent_y.parent = parent_x
        parent_x.rank += 1

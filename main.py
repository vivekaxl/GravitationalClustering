from Utilities import random_ranges
from random import choice
from Makeset_Union_Find import union, findset
from Point import Point

def generate_population(number_candidates, number_dimension, l=0, u=1):
    lo = [l] * number_dimension
    up = [u] * number_dimension
    population = [Point([random_ranges(lo[i], up[i]) for i in xrange(number_dimension)]) for _ in xrange(number_candidates)]
    assert(len(population) == number_candidates), "Generation failed"
    return population

def algorithm(number_candidates, number_dimensions, G=10 ** -4, deltaG=0.6, number_iteration = 50, epsilon = 10 ** -2 ):
    def move(pointa, pointb, gravitational_constant):
        def eq_2_22(positionx, positiony):
            # effect of y on x
            d = [y - x for x, y in zip(positionx, positiony)]
            mag_d = sum([x**2 for x in d]) ** 0.5
            return [x + (gravitational_constant/(mag_d ** 3)) * d_i for x, d_i in zip(positionx, d)]
        new_pointa = eq_2_22(pointa.location, pointb.location)
        new_pointb = eq_2_22(pointb.location, pointa.location)
        pointa.location = new_pointa
        pointb.location = new_pointb
        return pointa, pointb
    assert(number_candidates > 0), "Candidates can't be negative"
    assert(number_dimensions > 0), "Number of dimenstions can't be negative"

    population = generate_population(number_candidates, number_dimensions)

    for iter_no in xrange(number_iteration):
        print iter_no
        for i,pop in enumerate(population):
            x_j = pop
            x_k = choice(population[:i] + population[i+1:])
            x_j, x_k = move(x_j, x_k, G)
            if x_j.distance(x_k) < epsilon:
                union(x_j, x_k)
            assert(x_j.location == pop.location), "Something's wrong"
        G *= (1-deltaG)

    clusters = set()
    for pop in population:
        clusters.add(findset(pop))
    print "Number of clusters: ", len(clusters)


if __name__ == "__main__":
    algorithm(10000, 2)